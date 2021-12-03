from django.db import connection
import json
from api.models import Customer, Appointment, Artist, Tattoo, Ink, artiststats, tattooparlorstats, appointmenttattooview
from django.views.decorators.csrf import csrf_exempt
from users.models import User

@csrf_exempt
def call_show_appointments(date):
    cursor = connection.cursor()
    try:
        id = 0
        appointments = dict()
        cursor.execute("CALL InkItUp.Show_tattooparlor_Appointments('{}','{}');".format(User.Tattooparlor_cvr, date))
        for record in cursor.fetchall():
            id += 1
            appointments[id] = {"tattooparlor_name": record[0], "booking_date_time": record[1], "SessionLenght": record[2], "Artist": record[3], "Hourly_rate": record[4], "Customer_Name": record[5], "PhoneNumber": record[6], "Totalprice": record[7]}
        return json.dumps(appointments, indent=4, sort_keys=False, default=str)
    finally:
        cursor.close()

def call_Update_ink_storage(batchnumber):
    cursor = connection.cursor()
    try:
        cursor.execute("CALL InkItUp.Update_Ink_Storage('{}');".format(batchnumber))
    finally:
        cursor.close()

def call_Ink_Batchnumber_Callback(batchnumber):
    cursor = connection.cursor()
    try:
        id = 0
        tattoos = dict()
        cursor.execute("CALL InkItUp.InkBatchNumberCallBackk('{}');".format(batchnumber))
        for record in cursor.fetchall():
            id += 1
            tattoos[id] = {"Customer_CPR": record[0], "Name": record[1], "PhoneNumber": record[2], "DateTime": record[3], "IdTattoo": record[4], "Ink_BatchNumber": record[5]}
        return json.dumps(tattoos, indent=4, sort_keys=False, default=str)
    finally:
        cursor.close()


def call_Register_Tattoo_with_Ink(NewidTattoo, NewDescription, NewPlacementOnBody, NewAppointment_idAppointment, Inkbatchnumber):
    cursor = connection.cursor()
    try:
        cursor.execute("CALL InkItUp.RegisterTattooWithInk('{}','{}','{}','{}','{}');".format(NewidTattoo, NewDescription, NewPlacementOnBody, NewAppointment_idAppointment, Inkbatchnumber))
    finally:
        cursor.close()


# MONGODB -------------------------------

from pymongo import MongoClient
import certifi
# connect to the mongoclient
client = MongoClient('mongodb+srv://nadia:1234!@inkitup-mongodb.elev4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', tlsCAFile=certifi.where())

# get the database
db = client['InkItUp']
customer_collection = db["Customer"]
tattooparlor_collection = db["Tattooparlor"]
'''
def mongo_get_customer(date):
    if customer_collection.count({"appointments.datetime":date}):
        for x in customer_collection.aggregate([
            {"$match":{"appointments.datetime": date}},
            {"$project": {
                    "firstname" : 1,
                    "lastname": 1,
                }}]):
            return json.dumps(x, indent=2) 
    else:
        return "no app does not exist. Please enter a valid CPR"
'''

def mongo_get_customer(date):
    data = []
    if customer_collection.count({"appointments.datetime":date}):
        for x in customer_collection.find({"appointments.datetime":date}):
            data.append(x)
        return json.dumps(data, indent=2) 
    else:
        return "no app does not exist. Please enter a valid CPR"

def mongo_create_appointment(c_id, a_id, datetime, sessionlength, tattooparlorid, artistid):
    price = 0
    cus_details = tattooparlor_collection.find({"artists._id": artistid})
    
    for r in cus_details:
        for x in r["artists"]:
            if x["_id"] == artistid:
                price = ((int(x["price"])) * sessionlength)

    customer_collection.update({"_id": c_id}, {"$addToSet": {"appointments": {
        "_id": a_id,
        "datetime": datetime,
        "sessionLenght": sessionlength,
        "tattoparlor": {
            "_id": tattooparlorid
        },
        "artist": {
            "_id": artistid
        },
        "price": price,
        "tattoos": {}
    }}})
    print(f"New appointment created for Customer:{c_id}")
    return f"New appointment created for Customer:{c_id}"
'''
def mongo_send(client_id,account_number, _amount):
    cur_date = date.today().strftime("%Y-%m-%d")
    if cl.count({"_id":client_id}):
        if cl.count({"accounts.number": account_number}):
            amount = float(_amount)
        # print(cl.aggregate([{"$project": {"accounts": {"balance" : 1}}}]))
            cl.update({ "_id": client_id, "accounts.number": account_number}, {"$inc": { "accounts.$.balance": -amount}, "$set": {"accounts.$.lastUpdate": cur_date}})
            tr.insert({"_id":tr.count(), "account_number": account_number, "amount": amount, "status": "send", "date": cur_date, "client_id": client_id})
            
            return "Transaction Successful"
        else:
            return "Account doesnt exist. Please enter a valid account number."
    else :
        return "Client does not exist. Please enter a valid client ID"
'''