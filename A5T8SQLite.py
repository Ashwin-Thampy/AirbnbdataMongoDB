import sqlite3
import time


def execute_task(path, param):
    """
    Execute task 5
    """
    
    query = """SELECT l.host_name, l.price, r.comments from reviews r, listings l on l.id = r.listing_id where r.listing_id = (?) order by r.date DESC limit 1;"""

    query2 = "SELECT listing_id from reviews;"
    
    connection = sqlite3.connect(path) # connecting to database
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    
   
    
    # check if the listing exists
    cursor.execute(query2)
    rows = cursor.fetchall()
    exists = 0
    for row in rows:
        if row['listing_id'] == param:
            exists = 1
            
            
    if exists:
        #executing query
        start = time.time()
        cursor.execute(query, (param,))
        end = time.time() - start

        rows = cursor.fetchall()
        print("\nMost recent review for listing", param,":")
        # printing data
        for row in rows:
            print(row['host_name'], row['price'], row['comments'])
            print("\nTime taken to run query: ", end)
            print("\n")
    else:
        print("\nListing doesn't exists in the database\n")
        
def getTask():
    """
    get task seleted by user
    """

    valid = False
    while not valid:
        print("Tasks:\
            \n1)  Given a listing_id at run-time (e.g., using command line prompt or via an application parameter) find the host_name, rental_price and the most recent review for that listing.\
            \n2) Quit")                                         # display the 2 options
        task = input("Choose a Task (enter a number between 1-2): ")            # ask user to choose a task
        if task.isdigit() == True and 1 <= int(task) <= 2:
            valid = True # validate
    return task


def getID():
    valid = False
    while not valid:
        param = input("Enter a listing_id: ")
        if(param.isdigit()):
            return int(param)
        else:
            print("Invalid Input")
if __name__ == "__main__":
    path = "./A5.db"
    while True:
        task = int(getTask())
        if task == 1:
            param = getID()
            execute_task(path, param)
        elif task == 2:
            break