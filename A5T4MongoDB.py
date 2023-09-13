import pymongo
import time

def execute_task(client):
    """
    Execute task 3
    """

    db = client.A5db

    #executing query
    start = time.time()
    ids = db.listings.aggregate([{"$match": {"reviews": {"$exists": False}}}, {"$group": {"_id": {"listing_id": "$id"}}}, {"$sort": {"_id": 1}}, {"$limit":10}])
    for row in ids:
        print(row)     #Displaying the desired output for above query
    end = time.time() - start
    print("Time taken to run query: ", end)     #Printing the total time taken
    print("\n")

def getTask():
    """
    get task seleted by user
    """

    valid = False
    while not valid:
        print("\nTasks:\
            \n1) Find which listed property(ies) has(have) not received any review, order them by listing_id and output the top 10\.\
            \n2) Quit")  # display the 2 options
        task = input("\nChoose a Task (enter a number between 1-2): ")            # ask user to choose a task
        if task.isdigit() == True and 1 <= int(task) <= 2:
            valid = True
    return task



if __name__ == "__main__":
    client = pymongo.MongoClient('mongodb://localhost:27012')
    while True:
        task = int(getTask())      #Ask user to select a task
        if task == 1:
            execute_task(client)     #Execute the selected task
        elif task == 2:
            break

