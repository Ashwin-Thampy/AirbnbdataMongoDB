
import sqlite3
import csv

def create_listings(path):
    """
    create the table listing in the database
    """

    # queries
    create_table = """ CREATE table listings (
id integer,
name text,
host_id integer,
host_name text,
neighbourhood text,
room_type text,
price integer,
minimum_nights integer,
availability_365 integer,
PRIMARY KEY(id)); """

    insert_values = """INSERT INTO listings
(id, name, host_id, host_name, neighbourhood,
room_type, price, minimum_nights, availability_365)
VALUES (?,?,?,?,?,?,?,?,?); """
    
    drop_table = "DROP TABLE IF EXISTS listings;"

    # connecting database
    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    cursor.execute(drop_table) # dropping table if exists
    cursor.execute(create_table) # creating new table

    # reading the listing file.
    with open('YVR_Airbnb_listings_summary.csv', 'r') as fl:
        dic = csv.DictReader(fl)
        data = [(i['id'], i['name'], i['host_id'], i['host_name'], i['neighbourhood'], i['room_type'], i['price'], i['minimum_nights'], i['availability_365']) for i in dic]

    cursor.executemany(insert_values, data)

    connection.commit()
    connection.close()
    print("Listing table created")

def create_reviews(path):
    """
    create table reviews
    """

    # queries
    create_table = """ CREATE TABLE reviews (
listing_id integer,
id integer,
date date,
reviewer_id integer,
reviewer_name text,
comments text,
PRIMARY KEY(id),
FOREIGN KEY(listing_id) REFERENCES listings);"""

    drop_table = "DROP TABLE IF EXISTS reviews;"

    insert_table = """ INSERT INTO reviews
(listing_id, id, date, reviewer_id, reviewer_name, comments) VALUES (?,?,?,?,?,?);"""

    # connecting database
    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    cursor.execute(drop_table) # dropping table if exists
    cursor.execute(create_table) # creating table

    with open('YVR_Airbnb_reviews.csv', 'r') as fl:
        dic = csv.DictReader(fl)
        data = [(i['listing_id'], i['id'], i['date'], i['reviewer_id'], i['reviewer_name'], i['comments']) for i in dic]
        cursor.executemany(insert_table, data)

        connection.commit()
        connection.close()
        print("Review table created")
    
    
def checksum(path):
    """
    Not part of task but checking if the values inseretd in the tables are according to specification
    """
    conn = sqlite3.connect(path)   
    cur = conn.cursor()

    cur.execute("SELECT MIN(host_id), MAX(host_id), AVG(host_id), COUNT(host_id) FROM listings;")
    print(cur.fetchone())
    cur.execute("SELECT MIN(id), MAX(id), AVG(id), COUNT(id) FROM reviews")
    print(cur.fetchone())


if __name__ == "__main__":
    path = "./A5.db"
    create_listings(path)
    create_reviews(path)
    checksum(path)
