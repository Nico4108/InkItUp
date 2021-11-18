from django.db import connection
import json
from api.models import Customer, Appointment, Artist, Tattoo, Ink, artiststats, tattooparlorstats, appointmenttattooview
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def call_show_appointments(tattooparlorCVR, date):
    cursor = connection.cursor()
    try:
        id = 0
        appointments = dict()
        cursor.execute("CALL InkItUp.Show_tattooparlor_Appointments('{}','{}');".format(tattooparlorCVR, date))
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

'''
def call_Register_Tattoo_with_Ink(batchnumber):
    cursor = connection.cursor()
    try:
        id = 0
        tattoo = dict()
        cursor.execute("CALL InkItUp.InkBatchNumberCallBackk('{}');".format(batchnumber))
        for record in cursor.fetchall():
            id += 1
            tattoos[id] = {"Customer_CPR": record[0], "Name": record[1], "PhoneNumber": record[2], "DateTime": record[3], "IdTattoo": record[4], "Ink_BatchNumber": record[5]}
        return json.dumps(tattoos, indent=4, sort_keys=False, default=str)
    finally:
        cursor.close()
'''