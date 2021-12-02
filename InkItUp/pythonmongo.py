import pymongo
#connect_string = 'mongodb+srv://<username>:<password>@<atlas cluster>/<myFirstDatabase>?retryWrites=true&w=majority' 

from django.conf import settings
my_client = pymongo.MongoClient('mongodb+srv://nadia:1234!@inkitup-mongodb.elev4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')


# First define the database name
dbname = my_client['InkItUp_MongoDB']

# Now get/create collection name (remember that you will see the database in your mongodb cluster only after you create a collection
collection_name = dbname["appointmentfull"]

#let's create two documents
customer_1 = {
    "CPR": "456566",
    "Name" : "Paracetamol hold",
    "Email" : "test@test.dk",
    "PhoneNumber" : "14546544",
    "registered": "2017-01-20",
    "hehe": "det nice"
}
customer_2 = {
    "CPR": "45638893",
    "Name" : "hold adesen",
    "Email" : "tt@test.dk",
    "PhoneNumber" : "14546555",
    "registered": "2017-01-20",
    "hehe": "det makes no sense"
}
# Insert the documents
collection_name.insert_many([customer_1, customer_2])
# Check the count
count = collection_name.count()
print(count)

# Read the documents
cus_details = collection_name.find({})
# Print on the terminal
for r in cus_details:
    print(r["Name"])
# Update one document
# update_data = collection_name.update_one({'medicine_id':'RR000123456'}, {'$set':{'common_name':'Paracetamol 500'}})

# Delete one document
# delete_data = collection_name.delete_one({'medicine_id':'RR000123456'})
