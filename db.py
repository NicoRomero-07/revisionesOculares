import sqlalchemy as alch
from sqlalchemy import *


class db:
    def __init__(self, url):
        # url = 'mysql+pymysql://root:nicolaszhiliezhao@localhost:3306/mydb'
        self.engine = alch.create_engine(url)
        self.metadata = MetaData(self.engine)
        self.metadata.reflect()

    def execute(self, query):
        with self.engine.connect() as connection:
            return connection.execute(text(query)).all()
