from bottle import (
    route, run, template, request, redirect
)

from homework06.bayes import clean, NaiveBayesClassifier
from homework06.db import News, session
from homework06.scraputils import get_news


@route("/news")
def news_list():
    s = session()
    rows = s.query(News).filter(News.label == None).all()
    return template('./news_template.html', rows=rows)


@route("/add_label/")
def add_label():
    label = request.query.label
    id = request.query.id
    s = session()
    changing_news = s.query(News).get(id)
    changing_news.label = label
    s.commit()
    redirect("/news")


@route("/update")
def update_news():
    new_news_list = get_news("https://news.ycombinator.com/", n_pages=5)
    s = session()
    old_news = s.query(News).all()
    for news in new_news_list:
        for o_news in old_news:
            if (news['title'] == o_news.title and
                    news['author'] == o_news.author):
                break
        else:
            new_news = News(title=news['title'],
                            author=news['author'],
                            url=news['url'],
                            comments=news['comments'],
                            points=news['points'])
            s.add(new_news)
            s.commit()
    redirect("/news")


@route("/recommendations")
def recommendations():
    # 1. Получить список неразмеченных новостей из БД
    # 2. Получить прогнозы для каждой новости
    # 3. Вывести ранжированную таблицу с новостями
    s = session()
    none_news = []
    rows = s.query(News).filter(News.label == None).all()
    learn_news = s.query(News).filter(News.label != None).all()
    X_train, y_train = [], []
    for news in learn_news:
        X_train.append(news.title)
        y_train.append(news.label)
    X_train = [clean(x).lower() for x in X_train]
    model = NaiveBayesClassifier(alpha=1)
    model.fit(X_train, y_train)
    for news in rows:
        none_news.append(news.title)
    predict_labels = model.predict(none_news)
    for news, label in zip(rows, predict_labels):
        news.label = label
    classified_news = sorted(rows, key=lambda news: news.label)
    return template('./news_recommendations.html', rows=classified_news)




if __name__ == "__main__":
    run(host="localhost", port=8080)


