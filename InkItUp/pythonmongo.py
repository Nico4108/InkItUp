import pymongo
import certifi
#connect_string = 'mongodb+srv://<username>:<password>@<atlas cluster>/<myFirstDatabase>?retryWrites=true&w=majority' 

from django.conf import settings
my_client = pymongo.MongoClient('mongodb+srv://root:1234!@inkitup-mongodb.elev4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', tlsCAFile=certifi.where())


# First define the database name
dbname = my_client['InkItUp']

# Now get/create collection name (remember that you will see the database in your mongodb cluster only after you create a collection
collection_name = dbname["Customer"]
'''
#let's create two documents
Customer1 = {
        "_id": 5173,
        "name": "Miss Kelsie Okuneva,
        "phonenumber": "23785111",
        "email": "guy.terry@gmail.com",
        "registered": "2020-07-15",
        "appointments": 
            [
                {
                    "_id": 2,
                    "datetime": "2022-10-13 05:00:00",
                    "sessionlenght": "3",
                    "tattooparlor": {
                        "_id": 31111119
                    },
                    "artist": {
                         "_id": 40443201
                    },
                    "price": "5000",
                    "tattoos": [
                        {
                            "_id": 45,
                            "description": "gest gest gest. Voluptatem doloribus sequi voluptatem sit ipsa nostrum. Dolor earum ut maiores autem cumque. Sit fugit ut soluta commodi rerum nihil.",
                            "placementonbody": "foden",
                            "inks":
                            [
                                {
                                    "_id": 13468
                                }
                            ]
                        }
                    ]
                }
            ]      
}


# Insert the documents
collection_name.insert_many([Customer1])
# Check the count
count = collection_name.count()
print(count)
'''
# Read the documents
cus_details = collection_name.find({"appointments.datetime": "2022-10-13 05:00:00"})
# Print on the terminal
for r in cus_details:
    print(r["_id"])
# Update one document
# update_data = collection_name.update_one({'medicine_id':'RR000123456'}, {'$set':{'common_name':'Paracetamol 500'}})

# Delete one document
# delete_data = collection_name.delete_one({'medicine_id':'RR000123456'})
