import pymongo
#connect_string = 'mongodb+srv://<username>:<password>@<atlas cluster>/<myFirstDatabase>?retryWrites=true&w=majority' 

from django.conf import settings
my_client = pymongo.MongoClient('mongodb+srv://nadia:1234!@inkitup-mongodb.elev4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')


# First define the database name
dbname = my_client['InkItUp']

# Now get/create collection name (remember that you will see the database in your mongodb cluster only after you create a collection
collection_name = dbname["appointment"]

#let's create two documents
customer_1 = {
"appointment": {
        "_id": "6656",
        "dato": "2021-23-03 15:00:00",
        "session_length": "5",
        "customer": {
            "name": "Carsten Hansen",
            "email": "Eamil@mail.com",
            "phonenumber": "11223344",
            "registered": "2021-01-01 12:00:00"
        },
        "Tattooparlor": {
            "cvr": "615552967",
            "name": "Kims kinky bix",
            "phonenumber": "00998877",
            "email": "mailmail@gmail.com",
            "artist": {
                "cvr": "615552123",
                "name": "lil-Nadia funcky",
                "phonenumber": "11998877",
                "email": "lilnfuck@gmail.com",
                "price": {
                    "$numberInt": "1500"
                }
            }
        },
        "Tattoo": {
            "placement_on_body": "left arm",
            "id": "80",
            "description": "Very nice tattoo",
            "Ink": {
                "batchnumber": "619650",
                "color": "red",
                "excpiration_date": "2025-01-12",
                "price": {
                    "$numberInt": "1200"
                },
                "quantity": {
                    "$numberInt": "7"
                },
                "producer": {
                    "cvr": "61788767",
                    "name": "Svendes lange ink",
                    "phonenumber": "66776652",
                    "adress": "Lærkevej 5, Balladerup"
                }
            }
        }
    }
}

# Insert the documents
collection_name.insert_many([customer_1])
# Check the count
count = collection_name.count()
print(count)

# Read the documents
cus_details = collection_name.find({})
# Print on the terminal
for r in cus_details:
    print(r["_id"])
# Update one document
# update_data = collection_name.update_one({'medicine_id':'RR000123456'}, {'$set':{'common_name':'Paracetamol 500'}})

# Delete one document
# delete_data = collection_name.delete_one({'medicine_id':'RR000123456'})
