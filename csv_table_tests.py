"""

csv_table_tests.py

"""

from src.CSVDataTable import CSVDataTable

import os
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
data_dir = os.path.abspath("../Data/Baseball")


def tests_people():
    connect_info = {
        "directory": data_dir,
        "file_name": "People.csv"
    }
    people = CSVDataTable("People", connect_info, ["playerID"])
    try:

        # Find by primary key
        print()
        print("find_by_primary_key(): Known Record")
        print(people.find_by_primary_key(["aardsda01"]))

        print()
        print("find_by_primary_key(): Unknown Record")
        print(people.find_by_primary_key((["cah2251"])))

        #Find by template
        print()
        print("find_by_template(): Known Template")
        template = {"nameFirst": "David", "nameLast": "Aardsma", "nameGiven": "David Allan"}
        print(people.find_by_template(template))

        print()
        print("find_by_template(): Known Template")
        template = {"nameFirst": "David", "nameLast": "Aardsma", "nameGiven": "David Allan"}
        print(people.find_by_template(template))

        print()
        print("find_by_template(): Unknown Template")
        template = {"nameFirst": "Kyungjin", "nameLast": "Kim", "nameGiven": "Idontknow"}
        print(people.find_by_template(template))
        # Delete by template
        print()
        print("delete_by_template(): Known Template")
        template = {"nameFirst": "David", "nameLast": "Aardsma", "nameGiven": "David Allan"}
        print("Count of deletion: " + str(people.delete_by_template(template)))

        print()
        print("delete_by_template(): Unknown Template")
        template = {"nameFirst": "Kyungjin", "nameLast": "Kim", "nameGiven": "Idontknow"}
        print("Count of deletion: " + str(people.delete_by_template(template)))

        # Delete by key
        print()
        print("delete_by_key(): Known Record")
        key = ["aardsda01", "aaronto01"]
        print("Count of deletion: " + str(people.delete_by_key(key)))

        print()
        print("delete_by_key(): Known Record")
        key = ["abbated01"]
        print("Count of deletion: " + str(people.delete_by_key(key)))

        print()
        print("delete_by_key(): Unknown Record")
        key = ["kasda, asdads, asdsadsa"]
        print("Count of deletion: " + str(people.delete_by_key(key)))

        #update by template
        print()
        print("update_by_template(): known Template")
        template = {"playerID": "abercre01"}
        new_values = {"birthDay": "21", "birthState": "AZ"}
        print("Original Template: " + str(people.find_by_template(template, field_list=["birthDay", "birthState"])))
        people.update_by_template(template, new_values)
        print("Updated Template: " + str(people.find_by_template(template, field_list=["birthDay", "birthState"])))
        print("Count of update: " + str(people.update_by_template(template, new_values)))

        print()
        print("update_by_template(): Unknown Template")
        template = {"playerID": "asdasdsa"}
        new_values = {"birthDay": "21", "birthState": "AZ"}
        people.update_by_template(template, new_values)
        print("Updated Template: " + str(people.find_by_template(template, field_list=["birthDay", "birthState"])))
        print("Count of update: " + str(people.update_by_template(template, new_values)))

        #update by key

        print()
        print("update_by_key(): known Record")
        key = ["abbotji01", "abbotky01"]
        new_values = {"birthDay": "20", "birthState": "CA"}
        people.update_by_key(key, new_values)
        print("Count of update: " + str(people.update_by_key(key, new_values)))


        print()
        print("update_by_key(): Unknown Record")
        key = ["ccc11112", "abcdefg"]
        new_values = {"birthDay": "20", "birthState": "CA"}
        people.update_by_key(key, new_values)
        print("Count of update: " + str(people.update_by_key(key, new_values)))

        #inserd new record
        print()
        print("Insert new record - Unique Primary Key exists: ")
        record = {"playerID": "kjk0621", "birthYear": "1991", "birthMonth": "6", "birthDay": "21"}
        people.insert(record)
        print("Check if record is inserted: " + str(people.find_by_primary_key(["kjk0621"])))

        print()
        print("Insert new record - Duplicate Primary Key exists(do not insert): ")
        record = {"playerID": "abbotje01", "birthYear": "1991", "birthMonth": "6", "birthDay": "21"}
        people.insert(record)
        print("Check if record is inserted: " + str(people.find_by_primary_key(["abbotje01"])))

        print()
        print("Insert new record - Primary Key doesn't exist: ")
        record = {"birthYear": "1992", "birthMonth": "07", "birthDay": "23"}
        people.insert(record)
        print("Check if record is inserted(empty record): " + str(people.find_by_template(record)))

        # Please complete code IN THE SAME FORMAT to test when the rest of methods pass or fail
        # HINT HINT: Don't forget about testing the primary key integrity constraints!!
        # For these tests, think to yourself: When should this fail? When should this pass?

    except Exception as e:
        print("An error occurred:", e)


def tests_batting():
    connect_info = {
        "directory": data_dir,
        "file_name": "Batting.csv"
    }
    batting = CSVDataTable("Batting", connect_info, ["playerID"])
    try:

        # Find by primary key
        print()
        print("find_by_primary_key(): Known Record")
        print(batting.find_by_primary_key(["abercda01"]))

        print()
        print("find_by_primary_key(): Unknown Record")
        print(batting.find_by_primary_key((["ccc2251"])))

        #Find by template
        print()
        print("find_by_template(): Known Template")
        template = {"playerID": "addybo01", "yearID": "1871", "teamID": "RC1"}
        print(batting.find_by_template(template))

        print()
        print("find_by_template(): Known Template")
        template = {"playerID": "allisdo01", "yearID": "1871", "teamID": "WS3"}
        print(batting.find_by_template(template))

        print()
        print("find_by_template(): Unknown Template")
        template = {"playerID": "kjk0621", "yearID": "1991", "teamID": "WS5"}
        print(batting.find_by_template(template))
        # Delete by template
        print()
        print("delete_by_template(): Known Template")
        template = {"playerID": "bassjo01", "yearID": "1871", "teamID": "CL1"}
        print("Count of deletion: " + str(batting.delete_by_template(template)))

        print()
        print("delete_by_template(): Unknown Template")
        template = {"playerID": "asdsad012", "yearID": "1971", "teamID": "CL4"}
        print("Count of deletion: " + str(batting.delete_by_template(template)))

        # Delete by key
        print()
        print("delete_by_key(): Known Record")
        key = ["bellast01", "berkena01"]
        print("Count of deletion: " + str(batting.delete_by_key(key)))

        print()
        print("delete_by_key(): Known Record")
        key = ["biermch01"]
        print("Count of deletion: " + str(batting.delete_by_key(key)))

        print()
        print("delete_by_key(): Unknown Record")
        key = ["brasq1212, ksks1212, qrqr1212"]
        print("Count of deletion: " + str(batting.delete_by_key(key)))

        #update by template
        print()
        print("update_by_template(): known Template")
        template = {"playerID": "brannmi01"}
        new_values = {"yearID": "1941", "teamID": "CA4"}
        print("Original Template: " + str(batting.find_by_template(template, field_list=["yearID", "teamID"])))
        batting.update_by_template(template, new_values)
        print("Updated Template: " + str(batting.find_by_template(template, field_list=["yearID", "teamID"])))
        print("Count of update: " + str(batting.update_by_template(template, new_values)))

        print()
        print("update_by_template(): Unknown Template")
        template = {"playerID": "cscs123"}
        new_values = {"yearID": "1971", "teamID": "CZ4"}
        batting.update_by_template(template, new_values)
        print("Updated Template: " + str(batting.find_by_template(template, field_list=["yearID", "teamID"])))
        print("Count of update: " + str(batting.update_by_template(template, new_values)))

        #update by key

        print()
        print("update_by_key(): known Record")
        key = ["hamra01", "hastisc01"]
        new_values = {"yearID": "1971", "teamID": "CZ4"}
        batting.update_by_key(key, new_values)
        print("Count of update: " + str(batting.update_by_key(key, new_values)))


        print()
        print("update_by_key(): Unknown Record")
        key = ["ccc11112", "abcdefg"]
        new_values = {"yearID": "1971", "teamID": "CZ4"}
        batting.update_by_key(key, new_values)
        print("Count of update: " + str(batting.update_by_key(key, new_values)))

        #inserd new record
        print()
        print("Insert new record - Unique Primary Key exists: ")
        record = {"playerID": "kjk0101", "yearID": "1991", "teamID": "CRI"}
        batting.insert(record)
        print("Check if record is inserted: " + str(batting.find_by_primary_key(["kjk0101"])))

        print()
        print("Insert new record - Duplicate Primary Key exists(do not insert): ")
        record = {"playerID": "barre01", "yearID": "1872", "teamID": "BR2"}
        batting.insert(record)
        print("Check if record is inserted: " + str(batting.find_by_primary_key(["barre01"])))

        print()
        print("Insert new record - Primary Key doesn't exist: ")
        record = {"yearID": "1212", "teamID": "BR3"}
        batting.insert(record)
        print("Check if record is inserted(empty record): " + str(batting.find_by_template(record)))

        # Please complete code IN THE SAME FORMAT to test when the rest of methods pass or fail
        # HINT HINT: Don't forget about testing the primary key integrity constraints!!
        # For these tests, think to yourself: When should this fail? When should this pass?

    except Exception as e:
        print("An error occurred:", e)


tests_people()
tests_batting()
