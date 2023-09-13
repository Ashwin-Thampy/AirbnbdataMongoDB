import sqlite3
import time


def execute_task(path):
    """
    Execute task 3
    """
    
    query = """SELECT host, new_count FROM (
SELECT host_id as host, COUNT(host_id) as new_count
FROM listings
GROUP BY host_id
ORDER BY host_id
LIMIT 10)
ORDER BY host 
; """
    
    connection = sqlite3.connect(path) # connecting to database
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    #executing query
    start = time.time()
    cursor.execute(query)
    end = time.time() - start

    rows = cursor.fetchall()
    print("\nTop 10 host with the most listings: ")
    # printing data
    for row in rows:
        print(row['host'], row['new_count'])
    print("Time taken to run query: ", end)
    print("\n")

def getTask():
    """
    get task seleted by user
    """

    valid = False
    while not valid:
        print("Tasks:\
            \n1) Find how many listings each host own, ordering the output by host_id and only output the top 10.\
            \n2) Quit")                                         # display the 2 options
        task = input("Choose a Task (enter a number between 1-2): ")            # ask user to choose a task
        if task.isdigit() == True and 1 <= int(task) <= 2:
            valid = True
    return task



if __name__ == "__main__":
    path = "./A5.db"
    while True:
        task = int(getTask())
        if task == 1:
            execute_task(path)
        elif task == 2:
            break
