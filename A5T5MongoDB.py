import pymongo
import time

def execute_task(client, param):
    """
    Execute task 3
    """

    db = client.A5db

    #executing query
    start = time.time()
    avg_price = db.listings.aggregate([{"$match": {"neighbourhood": {"$in": [param]}}}, {"$group": {"_id": {"neighbourhood": param}, "avg_price": {"$avg": "$price"}}}])
    price_list = list(avg_price)
    if len(price_list) == 0:    #To check if enterd neighbourhood exists or not
        print("Entered neighbourhood %s doesn't exist" %(param))
        print("\nTry again!!!")
    else:
        print("Average price for %s:" %(param))    #Print the desired output
        for price in price_list:
                print(price) 
        end = time.time() - start
        print("Time taken to run query: ", end)      #Print the time tken to execute
    print("\n")

def getTask():
    """
    get task seleted by user
    """

    valid = False
    while not valid:
        print("\nTasks:\
            \n1) Given a neighbourhood at run-time (e.g., using command line prompt or via an application parameter) find the average rental cost/night\
            \n2) Quit")  # display the 2 options
        task = input("\nChoose a Task (enter a number between 1-2): ")            # ask user to choose a task
        if task.isdigit() == True and 1 <= int(task) <= 2:
            valid = True
    return task


def get_input():
    param = input("Enter a neighbourhood: ")
    return param

if __name__ == "__main__":
    client = pymongo.MongoClient('mongodb://localhost:27012')
    while True:
        task = int(getTask())     #Ask a user to select a task
        if task == 1:
            param = get_input()      #Ask user to enter a neighbourhood
            execute_task(client, param)     #Execute the selected task
        elif task == 2:
            break
