import pymongo
import time
import pprint

def execute_task(client, users_id):
    """
    Execute task 8
    """

    db = client.A5db
    exists = 0

    #executing query
    start = time.time()
    #Get only the review with the newest date, using the sort and limit variables
    newest_review = db.listings.aggregate([
    {'$match': {'id': users_id}},
    {'$unwind': "$reviews"},
    {'$sort': {'reviews.date': -1}},
    {"$limit":1}
    ])
    #If there is a review and the return wasn't completely empty, print it and change exists to true
    for review in newest_review:
        print('Host name:', review['host_name'])
        print('Price:', review['price'])
        print('The most recent review for the provided ID:')
        print(review['reviews']['comments'])
        exists = 1
    #If there is no review or no such ID in the database (newest_review is empty) let the user know
    if not exists:
        print('The listing id provided does not exist or does not have any reviews assigned to it.')
    end = time.time() - start
    print("Time taken to run query: ", end)
    print("\n")


def getTask():
    """
    get task seleted by user
    """

    valid = False
    while not valid:
        print("\nTasks:\
            \n1) Given a listing_id at run-time find the host_name, rental_price and the most recent review for that listing.\
            \n2) Quit")  # display the 2 options
        task = input("\nChoose a Task (enter a number between 1-2): ")            # ask user to choose a task
        if task.isdigit() == True and 1 <= int(task) <= 2:
            valid = True
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
    client = pymongo.MongoClient('mongodb://localhost:27012')
    while True:
        task = int(getTask())
        if task == 1:
            users_id = getID()
            execute_task(client, users_id)
        elif task == 2:
            break
