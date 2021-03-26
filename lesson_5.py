'''
****************************************************************************
*  Program  lessson_5.py                                                   *
*  Author   Baba                                                          *
*  Date     March 16, 2021                                                 *
*  Source   Realpython https://realpython.com/python-sql-libraries/#sqlite *
*  Description:                                                            *
*  This program is used to introduce Geniuses to using a                   *
*  database Structured Query Language (SQL).  The program                  *
*  imports the sqlite3 module which allows you to create                   *
*  and interact with an SQL Database                                       *
*                                                                          *
*  - The create_connection function is passed the                          *
*    path of the SQLite database file then it connects                     *
*    the app to an exixting SQLite3 database named hgp_pods                *
*    or if it;s not present it creates the database file                   *
*                                                                          *
*  - The execute_query function is passed the path and the                 *
*    query to implement; create_staff_member_table query and               *
*    add_staff_member query                                                *
*                                                                          *
*  - The execute_read function is passed the path and                      *
*    the display_staff_member query                                        *
****************************************************************************

'''

import sqlite3
from sqlite3 import Error

############### Function Definitions *******************
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


###################  Connect/Create to the Sqlite3 Database File *********************
connection = create_connection("/users/akarijohnson.hgs/sql_tutorial/oak8_pods.sqlite5")


##########################  Create staff table variable query ################
create_staff_member_table_query = """
CREATE TABLE IF NOT EXISTS staff (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  cell TEXT NOT NULL,
  position TEXT NOT NULL
);
"""
#################### Executive query to create staff table #################
execute_query(connection, create_staff_member_table_query) 


################# Create insert query to add staff members to staff table #######
add_staff_members_query = """
INSERT INTO
  staff (name,cell,position)
VALUES
  ('Baba','510.205.0980','Senior Innovation Educator'),
  ('Brandon','111.111.1111', 'Executive Director'),
  ('Hodari','(510) 435-2594','Curriculum Lead'),
  ('Akeeem','(415) 684-0505','Programs Director');
"""
####################  Execute insert staff members query ##################
execute_query(connection, add_staff_members_query) 
###
create_pod_leader_table_query = """
CREATE TABLE IF NOT EXISTS pod_leader (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  cell TEXT NOT NULL,
  position TEXT NOT NULL
);
"""

#################### Create insert query to add pod leaders to table ##################
add_pod_leader_query = """
INSERT INTO
  pod_leader (name,cell,position)
VALUES
  ('Jacore','(845) 200-6250','Pod Leader'),
  ('Gabe','(510) 326-5834', 'Pod Leader'),
  ('Aris','(510) 229-6359','Pod Leader'),
  ('Richard','(510)228-5623','Pod Leader'),
  ('Andrew','(925) 727-4611','Pod Leader');
"""

##################
execute_query(connection, create_pod_leader_table_query)

execute_query(connection, add_pod_leader_query)
########################
create_pod_member_table_query = """
CREATE TABLE IF NOT EXISTS pod (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  cell TEXT NOT NULL,
  position TEXT NOT NULL
);
"""

#################### Create insert query to add pod leaders to table ##################
add_pod_member_query = """
INSERT INTO
  pod (name,cell,position)
VALUES
  ('Akari Johnson','(510) 500-2206','Pod member'),
  ('Prince Fields','(510) 472-0804','Pod member'),
  ('Morris Jones','(925) 286-5922','Pod member'),
  ('Moussa Ndiaye','(123) 456-7890','Pod member'),
  ('Jacore Baptiste','(845) 200-6250','Pod member');
"""

##################
execute_query(connection, create_pod_member_table_query)

execute_query(connection ,add_pod_member_query)



########################### Display staff_member Query ##################### 
display_staff_query = "SELECT * from staff"
staff = execute_read_query(connection, display_staff_query)

display_leaders_query = "SELECT * from pod_leader"
leader = execute_read_query(connection, display_leaders_query)

display_members_query = "SELECT * from pod"
member = execute_read_query(connection, display_members_query)

for user in staff:
  print(user)

for user in leader:
  print(user)

for user in member:
  print(user)

execute_query(connection,'drop table staff')

execute_query(connection,'drop table pod')

execute_query(connection,'drop table pod_leader')
