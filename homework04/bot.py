import requests
import telebot
from bs4 import BeautifulSoup
from datetime import datetime
from telebot import apihelper


access_token = '965696888:AAGfuxg8heeJBX0MqU18fte8Bvtvsw8-cTQ'
apihelper.proxy = {'https':'http://78.41.53.39:8080'}
bot = telebot.TeleBot(access_token)


dict = {'/monday': '1day', '/tuesday': '2day', '/wednesday': '3day', '/thursday': '4day', '/friday': '5day', '/saturday': '6day'}
name_week = ['Понедельник', ' Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']



def get_page(group: str) -> str:
    now = datetime.now()
    week = datetime.date(now).isocalendar()[1]
    if week % 2 == 0:
        week = '2'
    else:
        week = '1'
    url = '{domain}/{group}/{week}/raspisanie_zanyatiy_{group}.htm'.format(
        domain='http://www.ifmo.ru/ru/schedule/0',
        week=week,
        group=group)

    response = requests.get(url)
    web_page = response.text
    return web_page


def parse_schedule_for_a_all_day(web_page, day):
    soup = BeautifulSoup(web_page, "html5lib")
    day = str(day) + "day"
    # Получаем таблицу с расписанием на любой день недели
    schedule_table = soup.find("table", attrs={"id": day})
    if not schedule_table:
        return
    
    # Время проведения занятий
    times_list = schedule_table.find_all("td", attrs={"class": "time"})
    times_list = [time.span.text for time in times_list]

    # Место проведения занятий
    locations_list = schedule_table.find_all("td", attrs={"class": "room"})
    locations_list = [room.span.text for room in locations_list]

    # Название дисциплин и имена преподавателей
    lessons_list = schedule_table.find_all("td", attrs={"class": "lesson"})
    lessons_list = [lesson.text.split('\n\n') for lesson in lessons_list]
    lessons_list = [', '.join([info for info in lesson_info if info]) for lesson_info in lessons_list]


    # Аудитория
    auditor_list = schedule_table.find_all("td", attrs={"class": "room"})
    auditor_list = [aud.dd.text for aud in auditor_list]
    return times_list, locations_list, lessons_list, auditor_list


@bot.message_handler(commands=['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'])
def get_day(message):
    try:
        """ Получить расписание на любой день """
        day, group = message.text.split()
        day = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'].index(day[1:]) + 1
        web_page = get_page(group)
        try:
            times_lst, locations_lst, lessons_lst, auditor_list = parse_schedule_for_a_all_day(web_page, day)
        except Exception:
            bot.send_message(message.chat.id, 'На данный день нет пар')
            return
        resp = '#######<b>{}</b>####### \n\n\n'.format(name_week[day-1])
        for time, location, lession, auditor in zip(times_lst, locations_lst, lessons_lst, auditor_list):
            resp += '<b>{}</b>, {} <i>{}</i> {} \n\n'.format(time, location, lession, auditor)
        bot.send_message(message.chat.id, resp, parse_mode='HTML')
    except Exception:
        bot.send_message(message.chat.id, 'Вы ввели неверные данные\n повторите ввод даных')



@bot.message_handler(commands=['tomorrow'])
def get_tomorrow(message):
    """ Получить расписание на следующий день """
    _, group = message.text.split()
    web_page = get_page(group)
    day = datetime.today().isoweekday() + 1
    if day == 8:
        day = 1
    try:
        times_lst, locations_lst, lessons_lst, auditor_lst = parse_schedule_for_a_all_day(web_page, day)
    except Exception:
        bot.send_message(message.chat.id, 'На завтрашний день нет пар')
        return
    resp = '#######<b>{}</b>####### \n\n\n'.format(name_week[day-1])
    for time, location, lession, auditor in zip(times_lst, locations_lst, lessons_lst, auditor_lst):
        resp += '<b>{}</b>, {} <i>{}</i> {} \n\n'.format(time, location, lession, auditor)
    bot.send_message(message.chat.id, resp, parse_mode='HTML')



@bot.message_handler(commands=['all'])
def get_all_schedule(message):
    """ Получить расписание на всю неделю для указанной группы """
    _, group = message.text.split()
    web_page = get_page(group)
    resp = ''
    try:
        for day in range(1, 8):
            schedule_for_day = parse_schedule_for_a_all_day(web_page, day)
            if not schedule_for_day:
                continue
            times_lst, locations_lst, lessons_lst, auditor_lst = parse_schedule_for_a_all_day(web_page, day)
            times_lst, locations_lst, lessons_lst, aud_lst = schedule_for_day
            resp += '#######{}####### \n\n\n'.format(name_week[day-1])
            for time, location, lession, auditor in zip(times_lst, locations_lst, lessons_lst, auditor_lst):
                resp += '{}, {} {} {} \n\n'.format(time, location, lession, auditor)
        bot.send_message(message.chat.id, resp, parse_mode='HTML')
    except Exception:
        bot.send_message(message.chat.id, resp, 'Вы ввели неверные данные')


@bot.message_handler(commands=['near'])
def get_near_lesson(message):
    """ Получить ближайшее занятие """
    hour_now = datetime.now().hour * 60
    min_now = datetime.now().minute
    sum_now = (hour_now + min_now)
    ref_time =[]
    resp = ''
    _, group = message.text.split()
    web_page = get_page(group)
    day = datetime.today().isoweekday()
    try:                                                                                                      
        times_lst, locations_lst, lessons_lst, auditor_lst = parse_schedule_for_a_all_day(web_page, day)
    except Exception:
        bot.send_message(message.chat.id, 'На завтрашний день нет пар')
        return
    for dtimes in times_lst:
        dtimes = dtimes.split('-')
        dtimes = datetime.strptime(dtimes[0], '%H:%M')
        dtimes = tuple([dtimes.hour, dtimes.minute])
        ref_time.append(dtimes[0]*60 + dtimes[1])
    for rmin in ref_time:
            if sum_now < rmin:
                for time, location, lession, auditor in zip(times_lst, locations_lst, lessons_lst, auditor_lst):
                    resp += '<b>{}</b>, {} <i>{}</i> {} \n\n'.format(time, location, lession, auditor)
                    bot.send_message(message.chat.id, resp, parse_mode='HTML')
                    exit()
            else:
                 bot.send_message(message.chat.id,'Пары кончились')
                 exit()


if __name__ == '__main__':
    bot.polling(none_stop=True)