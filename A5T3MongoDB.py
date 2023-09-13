import pymongo
import time

def execute_task(client):
    """
    Execute task 3
    """
    
    db = client.A5db
    
    #executing query
    start = time.time()
    hosts = db.listings.aggregate([{"$group": {"_id":{"host": "$host_id"}, "total_listings": {"$sum": 1}}}, {"$sort": {"_id":1}}, {"$limit": 10}])
    for row in hosts:
        print(row)   #printing the desired output after executing the above query
    end = time.time() - start
    print("Time taken to run query: ", end)     #Calculating total run time
    print("\n")
    
def getTask():
    """
    get task seleted by user
    """

    valid = False
    while not valid:
        print("\nTasks:\
            \n1) Find how many listings each host own (output only 10 in ascending order).\
            \n2) Quit")  # display the 2 options
        task = input("\nChoose a Task (enter a number between 1-2): ")            # ask user to choose a task
        if task.isdigit() == True and 1 <= int(task) <= 2:
            valid = True
    return task



if __name__ == "__main__":
    client = pymongo.MongoClient('mongodb://localhost:27012')
    while True:
        task = int(getTask())    #Ask user to select a task
        if task == 1:
            execute_task(client)      #Execute the selected task
        elif task == 2:
            break


