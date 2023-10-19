import mysql.connector
import random
from datetime import datetime, timedelta
import sys


def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='password',
            database='ServiceTicket'
        )
        
        if connection.is_connected():
            return connection

    except mysql.connector.Error as err:
        print(f"Error: {err} \nProgram will exit.")
        sys.exit(1)
    

def fetch_column_table(cursor, column, table):
    cursor.execute(f"SELECT {column} FROM {table}")
    data = cursor.fetchall()
    return [item[0] for item in data]

def valid_user_input(prompt = "Enter a value: ", input_type = "integer", min = 0, max = 0):
    while True:
            try:
                value = input(f"{prompt}")
                if(input_type == "integer"):
                    if min <= (value := int(value)) <= max:
                        return value
                    else:
                        print(f"Number is out of range. Please enter a number between {min} and {max}.")
                elif(input_type == "timestamp"):
                    valid_timestamp = datetime.strptime(value, "%Y-%m-%d").date()
                    return valid_timestamp
                else:   
                        return value
            except ValueError:
                print("Invalid input. Make sure you are using the proper format or input type.")


def generate_random_tickets(cursor, templates, amount, start_date, end_date):
    choices = {}
    for table, values in templates.items():
        for column in values:
            choices[column] = fetch_column_table(cursor, column, table)

    for key, values in choices.items():
        print(f"{key} : {values}")
    

if __name__ == "__main__":
    connection = connect_to_database()
    cursor = connection.cursor()
    templates = {'EventActivity': ['Activityname'], 
                 'EventOrigin' : ['OriginName'],
                 'EventStatus' : ['Status'],
                 'EventClass' : ['Class']
                 }

    number_of_tickets = 10#valid_user_input("Enter number of tickets to generate: ", min = 0, max = sys.maxsize)
    start_date = "2023-05-01"#valid_user_input("Enter start date in the format YYYY-MM-DD: ", "timestamp")
    end_date = "2023-09-01"#valid_user_input("Enter end date in the format YYYY-MM-DD: ", "timestamp")
    
    generate_random_tickets(cursor, templates, number_of_tickets, start_date, end_date)

    cursor.close()
    connection.close()



    
  

  

    
    