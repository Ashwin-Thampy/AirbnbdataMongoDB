import pymongo
import time
import pprint

def execute_task(client, words):
    """
    Execute task 8
    """
    db = client.A5db

    #executing query
    start = time.time()
    #Create the index that we will use to search based on text relevancy
    db.listings.create_index([('reviews.comments', pymongo.TEXT)], name='search_index', default_language='english')
    #Search for text relevancy on our index, limiting it to the top 3 options
    results = db.listings.aggregate([
        {'$match': {'$text': {'$search': words}}},
        {'$sort': {'score': {'$meta': 'textScore'}}},
        {'$limit': 3}
        ])
    #Print the results
    print('The top three most relevant result IDs are:')
    for row in results:
        print(row['id'])
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
            \n1) Find the top 3 listings which have reviews most similar to a set of keywords given at run-time. Assume those keywords will be given in a comma separated string.\
            \n2) Quit")  # display the 2 options
        task = input("\nChoose a Task (enter a number between 1-2): ")            # ask user to choose a task
        if task.isdigit() == True and 1 <= int(task) <= 2:
            valid = True
    return task

def get_words():
    words = input("Enter each Keywords separated by a ',': ")
    return words


if __name__ == "__main__":
    client = pymongo.MongoClient('mongodb://localhost:27012')
    while True:
        task = int(getTask())
        if task == 1:
            words = get_words()
            execute_task(client, words)
        elif task == 2:
            break
