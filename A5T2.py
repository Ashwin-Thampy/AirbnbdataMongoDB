import pymongo
import csv

def create_listings(client):
        '''
        Create collection for reviews
        '''
        #Connect the db to the function
        db = client.A5db
        listings = db.listings
        #Record the summaries table as a dictionary to be loaded into the database
        with open('YVR_Airbnb_listings_summary.csv', 'r') as fl:
                dic = csv.DictReader(fl)
                #Turn the DictReader ADT into a regular list
                data = [(i['id'], i['name'], i['host_id'], i['host_name'], i['neighbourhood'], i['room_type'], i['price'], i['minimum_nights'], i['availability_365']) for i in dic]
                #Finish turning the DictReader ADT into a regular list of dictionaries to make it easy to use
                db_data = []
                for i in range(0, len(data)):
                        db_data.append({'id': int(data[i][0]),
                                        'name': data[i][1],
                                        'host_id': int(data[i][2]),
                                        'host_name': data[i][3],
                                        'neighbourhood': data[i][4],
                                        'room_type': data[i][5],
                                        'price': int(data[i][6]),
                                        'minimum_nights': int(data[i][7]),
                                        'availability_365': int(data[i][8])})
                fl.close()
        #For the reviews, create a list of dictionaries to be embedded into the summaries as "reviews:"
        with open('YVR_Airbnb_reviews.csv', 'r') as fl:
                dic = csv.DictReader(fl)
                data = [(int(i['listing_id']), int(i['id']), i['date'], int(i['reviewer_id']), i['reviewer_name'], i['comments']) for i in dic]
                #Since the listing_id's are sorted, start from the lowest values and continue up the list that way
                current_listing = data[0][0]
                current_listing_number = 0
                info_to_embed = []
                for i in range(0, len(data)):
                        #If the current listing we're gathering the reviews for isn't the new one, we have to take some action
                        if (current_listing != data[i][0]):
                                #First make sure that the next listing in the db_data list is the next one (there can exist listings with no reviews)
                                while (current_listing != db_data[current_listing_number]['id']):
                                        current_listing_number += 1
                                #After making sure it is the next one, add the list of dictionaries of the reviews as an embedded list under its listing_id
                                db_data[current_listing_number]['reviews'] = info_to_embed
                                #Then reset it for the next listing_id
                                info_to_embed = []
                                current_listing_number += 1
                                current_listing = data[i][0]
                        #Add the current review info to the list to be embedded under its listing_id
                        info_to_embed.append({'id': data[i][1],
                                                'date': data[i][2],
                                                'reviewer_id': data[i][3],
                                                'reviewer_name': data[i][4],
                                                'comments': data[i][5]})
                fl.close()
        listings.insert_many(db_data)

'''
def checkdb(client):
        db = client.A5db
        x = db.reviews.aggregate([
                {'$group': {'_id': 'null', 'min': {'$min': "$host_id"}, 'max': {'$max': "$host_id"}, 'avg': {'$avg': "$host_id"}, 'count': {'$sum': 1}}}
        ])
        print(x)
        x = db.reviews.aggregate([
                {'$unwind': "$reviews"}, 
                {'$group': {'_id': 'null', 'min': {'$min': "$reviews.id"}, 'max': {'$max': "$reviews.id"}, 'avg': {'$avg': "$reviews.id"}, 'count': {'$sum': 1}}}
        ])
        print(x)
'''

if __name__ == "__main__":
        client = pymongo.MongoClient('mongodb://localhost:27012')
        create_listings(client)
        #checkdb(client)
