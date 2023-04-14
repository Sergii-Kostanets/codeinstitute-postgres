import os
from sqlalchemy import (
    create_engine, Column, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
if os.path.exists("env.py"):
    import env


password = os.environ.get("PASSWORD")
# Replace "username" and "password" with your actual credentials
username = "postgres"
password = password
host = "localhost"
port = 5432
database = "chinook"
# Create the database engine with the connection string including the password
db = create_engine(
    f"postgresql://{username}:{password}@{host}:{port}/{database}"
)


# executing the instructions from our localhost "chinook" db
# db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for the "Programmer" table
class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (db)
Session = sessionmaker(db)
# open an actual session by callin the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

# creating records on our Programmer table
ada_lovelace = Programmer(
    first_name="Ada",
    last_name="Lovelace",
    gender="F",
    nationality="British",
    famous_for="First Programmer"
)

alan_turing = Programmer(
    first_name="Alan",
    last_name="Turing",
    gender="M",
    nationality="British",
    famous_for="Modern Computing"
)

grace_hopper = Programmer(
    first_name="Grace",
    last_name="Hopper",
    gender="F",
    nationality="American",
    famous_for="COBOL language"
)

margaret_hamilton = Programmer(
    first_name="Margaret",
    last_name="Hamilton",
    gender="F",
    nationality="American",
    famous_for="Appolo 11"
)

bill_gates = Programmer(
    first_name="Bill",
    last_name="Gates",
    gender="M",
    nationality="American",
    famous_for="Microsoft"
)

tim_berners_lee = Programmer(
    first_name="Tim",
    last_name="Berners-Lee",
    gender="M",
    nationality="British",
    famous_for="World Wide Web"
)

sergii_kostanets = Programmer(
    first_name="Sergii",
    last_name="Kostanets",
    gender="M",
    nationality="Ukrainian",
    famous_for="Unknown... yet"
)

# add each instance of our programmers to the session
# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(sergii_kostanets)

# commit the session to the database
# session.commit()


# updating a single record
# programmer = session.query(Programmer).filter_by(id=7).first()
# programmer.famous_for = "Moving to Ireland"

# commit the session to the database
# session.commit()


# updating multiple records
# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender == "Male"
#     else:
#         print("Gender not defined")
#     session.commit()


# deleting a single record
# fname = input("Enter the first name of the programmer you want to delete: ")
# lname = input("Enter the last name of the programmer you want to delete: ")
# programmer = session.query(Programmer).filter_by(
#     first_name=fname, last_name=lname).first()

# defensive programming
# if programmer is not None:
#     print(
#         "Programmer found: ", programmer.first_name, programmer.last_name
#     )
#     confirmation = input(
#         "Are you sure you want to delete this record? (y/n): "
#     )
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Record deleted.")
#     else:
#         print("Record not deleted.")
# else:
#     print("Programmer not found.")


# deleting multiple records
# programmers = session.query(Programmer)
# for programmer in programmers:
#     session.delete(programmer)
#     session.commit()


# query the database to find All programmers
programmers = session.query(Programmer).order_by(Programmer.id).all()
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
    )
