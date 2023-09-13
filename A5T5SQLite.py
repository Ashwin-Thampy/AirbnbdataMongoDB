import sqlite3
import time


def execute_task(path, param):
    """
    Execute task 5
    """
    
    query = """SELECT AVG(price)
FROM listings
WHERE neighbourhood = (?); """

    query2 = "SELECT neighbourhood from listings;"
    
    connection = sqlite3.connect(path) # connecting to database
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    #checking if inputted neighbourhood exists in data
    cursor.execute(query2)
    rows = cursor.fetchall()
    exists = 0
    for row in rows:
        if param == row['neighbourhood']:
            exists = 1

    if exists:
        #executing query
        start = time.time()
        cursor.execute(query, (param,))
        end = time.time() - start
    
        rows = cursor.fetchall()
        print("\nAverage price for", param,":")
        # printing data
        for row in rows:
            print(row['AVG(price)'])
            print("Time taken to run query: ", end)
            print("\n")
    else:
        print("\nGiven neighbourhood doesn't exist in database\n")

        
def getTask():
    """
    get task seleted by user
    """

    valid = False
    while not valid:
        print("Tasks:\
            \n1)  Given a listing_id at run-time (e.g., using command line prompt or via an application parameter) find the host_name, rental_price and the most recent review for that listing.\
           2) Quit")                                         # display the 2 options
        task = input("Choose a Task (enter a number between 1-2): ")            # ask user to choose a task
        if task.isdigit() == True and 1 <= int(task) <= 2:
            valid = True # validate
    return task


def get_input():
    param = input("Enter a neighbourhood: ")
    return param
           
            
if __name__ == "__main__":
    path = "./A5.db"
    while True:
        task = int(getTask())
        if task == 1:
            param = get_input()
            execute_task(path, param)
        elif task == 2:
            break
