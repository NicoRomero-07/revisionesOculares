import sqlalchemy as alch
from sqlalchemy import *


class db:
    def __init__(self):
        url = 'mysql://root:1234@localhost:3306/mydb'
        self.engine = alch.create_engine(url)
        self.metadata = MetaData(self.engine)
        self.metadata.reflect()

    def execute(self, query):
        with self.engine.connect() as connection:
            connection.execute(text(query))

    def query(self, query):
        with self.engine.connect() as connection:
            return connection.execute(text(query)).all()

    def update(self, stmt):
        conn = self.engine.connect()
        conn.execute(stmt)
