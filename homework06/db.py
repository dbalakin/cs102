from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from homework06.scraputils import get_news

Base = declarative_base()
engine = create_engine("sqlite:///news.db")
session = sessionmaker(bind=engine)


class News(Base):
    __tablename__ = "news"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    url = Column(String)
    comments = Column(Integer)
    points = Column(Integer)
    label = Column(String)

Base.metadata.create_all(bind=engine)

def put_in_bd():
    s = session()
    news = get_news("https://news.ycombinator.com/news?p=1", n_pages=1)
    for el in news:
        item = News(title=el['title'],
                    author=el['author'],
                    url=el['url'],
                    comments=el['comments'],
                    points=el['points'])
        s.add(item)
        s.commit()


put_in_bd()