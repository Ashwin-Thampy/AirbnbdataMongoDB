Assignment #5

Group Member 1:
Name: Ashwin Thampy
Ccid: thampy
Collaboration Statement: Made References from
                         https://stackoverflow.com/questions/44575313/mongo-aggregate-match-after-sort-limit
                         https://docs.mongodb.com/manual/reference/operator/query/exists/
                         https://docs.mongodb.com/manual/reference/operator/aggregation/match/
                         https://www.geeksforgeeks.org/how-to-check-if-the-pymongo-cursor-is-empty/

Group Member 2:
Name: Aron Rajabi
Ccid: rajabi
Collaboration Statement: Made References from
https://docs.mongodb.com/manual/tutorial/text-search-in-aggregation/
https://stackoverflow.com/questions/8109122/how-to-sort-mongodb-with-pymongo
https://stackoverflow.com/questions/33541290/how-can-i-create-an-index-with-pymongo
https://docs.mongodb.com/manual/reference/method/db.collection.aggregate/
https://www.tutorialspoint.com/mongodb-query-to-set-user-defined-variable-into-query
https://courses.cs.washington.edu/courses/cse140/13wi/csv-parsing.html
https://docs.mongodb.com/manual/tutorial/model-embedded-one-to-many-relationships-between-documents/
https://pymongo.readthedocs.io/en/stable/tutorial.html#bulk-inserts

Group Member 3:
Name: Pranav Wadhwa
CCID: pwadhwa
Collaboration Statement: Made References from
For ingesting data from CSV File:
https://stackoverflow.com/questions/2887878/importing-a-csv-file-into-a-sqlite3-database-table-using-python



Files Included (beside this README.txt):
A5T1.py
A5T2.py
A5T3MongoDB.py
A5T3SQLite.py
A5T4MongoDB.py
A5T4SQLite.py
A5T5Mongo.py
A5T5SQLite.py
A5T8MongoDB.py
A5T8SQLite.py
A5T9MongoDB.py


IMPORTANT: The MongoDB server for all the tasks involving mongoDB as well as task 2 that creates the mongoDB database is ran on server port 27012 as opposed to the default 27017


'How to Guide':

A5T1.pt
This program requires YVR_Airbnb_listings_summary.csv and YVR_Airbnb_reviews.csv to make the SQL database. Just run the program and it will create 1 database and 2 tables ('listings' and 'reviews'). It also executes the statements given in the assignment description to check if all the correct values are in the database.

A5T2.py-
This program requires YVR_Airbnb_listings_summary.csv and YVR_Airbnb_reviews.csv to be in the same folder as it, and it will create the MongoDB database using server port 27012. It will create 1 single collection containing each column from YVR_Airbnb_listings_summary.csv, and then embeds every review from YVR_Airbnb_reviews.csv into the matching listing_ids with no input from the user. If a listing_id does not contain any reviews, an embedded review column will not be created for it.

A5T3SQLite.py
This code will provide the user with 2 options. 1) Find how many listings each host owns, ordering the output by host_id and only output the top 10 and 2) Quit.
option 1) will group the database according to host_id and calculate total listings for each host_id, then it will order the result in ascending order and print
the top 10 results. Option 2) will exit the code.

A5T3MongoDB.py-
This code will provide the user with 2 options. 1) Find how many listings each host own, ordering the output by host_id and only output the top 10 and 2) Quit.
option 1) will group the database according to host_id and calculate total listings for each host_id, then it will order the result in ascending order and print 
the top 10 results. Option 2) will exit the code. 

A5T4SQLite.py
This code will provide the user with 2 options. 1) Find which listed property(ies) has(have) not received any review, order them by listing_id and output the top 10
2) Quit. Option 1) will find listings with no reviews, order their listing_ids in ascending order and output the top 10 results. Option 2) will exit the code.

A5T4MongoDB.py-
This code will provide the user with 2 options. 1) Find which listed property(ies) has(have) not received any review, order them by listing_id and output the top 10
2) Quit. Option 1) will find listings with no reviews, order their listing_ids in ascending order and output the top 10 results. Option 2) will exit the code. 

A5T5SQLite.py
This code will provide the user with 2 options. 1) Given a neighbourhood at run-time  find the average rental cost/night?
2) Quit. Option 1) will ask the user to input a neighbourhood to calculate the average cost. If the neighbourhood is not present in the database it will throw out an error message. Option 2) will exit the code.

A5T5MongoDB.py-
This code will provide the user with 2 options. 1) Given a neighbourhood at run-time (e.g., using command line prompt or via an application parameter) find the average 
rental cost/night 2) Quit. Option 1) will ask the user to enter a valid neighbourhood (will give an error message for invalid input) and then output the average rental
cost/night for the entered neighbourhood. Option 2) will exit the code.  

A5T8SQLite.py
This code will provide the user with 2 options. 1) Given a listing_id at run-time find the host_name, rental_price and the most recent review for that listing.
2) Quit. Option 1) will ask the user to input a listing_id to find the host_name, rental_price and most recent review. If the listing_id is not present in the database it will throw out an error message. Option 2) will exit the code.

A5T8MongoDB.py-
When run, the program will ask the user to input 1 or 2 with descriptions of the options. 2 will quit the program, 1 will ask the user to input a listing_id. If the listing_id exists, it will output the host name, price per night, and the comments from the most recent review for the ID given.

A5T9MongoDB.py-
When run, the program will ask the user to input 1 or 2 with descriptions of the options. 2 will quit the program, 1 will ask the user to input a sequence of words with each word separated by a comma and a space. Then, the program will output the 3 listing_ids where the reviews.comments for the listing_ids match the words given by the user the most, using MongoDBs own built-in relevancy tracker from an index on reviews.comments and the meta score.


