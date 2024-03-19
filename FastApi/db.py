from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

sql_database_url="mysql://root:@localhost:3306/kishan"
engine=create_engine(sql_database_url)
session=sessionmaker(autocommit=False,bind=engine)
base=declarative_base()

