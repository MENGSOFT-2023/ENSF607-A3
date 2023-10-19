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

def generate_random_tickets(connection, cursor, templates, amount, start_date, end_date):
    choices = {'Caseid' : set()} # Using a set to obatain O(1) lookup speed
    for table, values in templates.items():
        for column in values:
            if column == 'Activityname':
                choices['Activity'] = dict(zip(fetch_column_table(cursor, 'ID', table), fetch_column_table(cursor, column, table)))
            choices[column] = fetch_column_table(cursor, column, table)

    for _ in range(amount):
        while (Caseid:=f"CS_{random.randint(1000000, 9999999)}") in choices['Caseid']:
            pass
        choices['Caseid'].add(Caseid)
        ID = random.choice(list(choices['Activity'].keys()))
        Activity = choices['Activity'][ID]
        Urgency = random.choice([1, 2, 3])
        Impact = random.choice([1, 2, 3])
        Priority = Urgency + Impact -1
        StartDate = random_date(start_date, end_date-timedelta(days=1))
        EndDate = random_date(StartDate + timedelta(days=1), end_date)
        Duration = (EndDate - StartDate).days
        TicketStatus = random.choice(choices['Status'])
        UpdateDateTime = random_timestamp(StartDate, EndDate)
        Origin = random.choice(choices['OriginName'])
        Class = random.choice(choices['Class'])

        # Uncomment for testing
        # print(ID, Caseid, Activity, Urgency, Impact, Priority, StartDate, EndDate, TicketStatus, UpdateDateTime, Duration, Origin, Class)

        # Insert statement
        insert_stmt = (
            "INSERT INTO EventLog (Caseid, Activity, Urgency, Impact, Priority, StartDate, EndDate, TicketStatus, UpdateDateTime, Duration, Origin, Class)"
            " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        )
        
        # Bind values to the statement
        data = (Caseid, Activity, str(Urgency), str(Impact), str(Priority), StartDate, EndDate, TicketStatus, UpdateDateTime, Duration, Origin, Class)

        # Execute the statement
        cursor.execute(insert_stmt, data)
        
    # Commit the transaction
    connection.commit()

def random_date(start_date, end_date):
    days_between_dates = (end_date - start_date).days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + timedelta(days=random_number_of_days)
    return random_date

def random_timestamp(start_date, end_date):
    days_between_dates = (end_date - start_date).days
    random_number_of_seconds = random.randrange((days_between_dates * 24 * 60 * 60))
    timestamp_start_date = datetime(start_date.year, start_date.month, start_date.day)
    random_timestamp = timestamp_start_date + timedelta(seconds=random_number_of_seconds)
    return random_timestamp

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

if __name__ == "__main__":
    connection = connect_to_database()
    cursor = connection.cursor()
    templates = {'EventActivity': ['Activityname'], 
                 'EventOrigin' : ['OriginName'],
                 'EventStatus' : ['Status'],
                 'EventClass' : ['Class']
                 }

    number_of_tickets = valid_user_input("Enter number of tickets to generate: ", min = 0, max = 8999999)
    start_date = valid_user_input("Enter start date in the format YYYY-MM-DD: ", "timestamp")
    end_date = valid_user_input("Enter end date in the format YYYY-MM-DD: ", "timestamp")

    # Uncoment for testing only
    #number_of_tickets = 1000
    #start_date = datetime.strptime("2023-05-01", "%Y-%m-%d").date()
    #end_date = datetime.strptime("2023-09-01", "%Y-%m-%d").date()
  
    generate_random_tickets(connection, cursor, templates, number_of_tickets, start_date, end_date)

    cursor.close()
    connection.close()



    
  

  

    
    