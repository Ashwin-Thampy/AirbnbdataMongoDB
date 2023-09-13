import sqlite3
import time


def execute_task(path):
    """
    Execute task 4
    """
    
    query = """SELECT id
FROM listings
WHERE id not in (SELECT listing_id as id from reviews)
LIMIT 10; """
    
    connection = sqlite3.connect(path) # connecting to database
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    #executing query
    start = time.time()
    cursor.execute(query)
    end = time.time() - start

    rows = cursor.fetchall()
    # printing data
    for row in rows:
        print(row['id'])
    print("Time taken to run query: ", end)
    print("\n")

def getTask():
    """
    get task seleted by user
    """

    valid = False
    while not valid:
        print("Tasks:\
            \n1) Find which listed property(ies) has(have) not received any review, order them by listing_id and output the top 10\
            \n2) Quit")                                         # display the 2 options
        task = input("Choose a Task (enter a number between 1-2): ")            # ask user to choose a task
        if task.isdigit() == True and 1 <= int(task) <= 2:
            valid = True # validate
    return task



if __name__ == "__main__":
    path = "./A5.db"
    while True:
        task = int(getTask())
        if task == 1:
            execute_task(path)
        elif task == 2:
            break            
