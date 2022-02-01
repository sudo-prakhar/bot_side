import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime

#TODO: set X & Y as 0 on complete
def nav_listener(event):
    '''
    Event listener that reacts to changes in event db events
    Everytime an event is called, it sends a 
    '''
    print("DATA: {} TIME: {}".format(event.data, datetime.now().strftime("%H:%M:%S")))

if __name__ == "__main__":

    cred = credentials.Certificate("keys/touri-65f07-firebase-adminsdk-wuv71-3751c21aa8.json")
    firebase_admin.initialize_app(cred, {'databaseURL': 'https://touri-65f07-default-rtdb.firebaseio.com/'})

    db.reference("/nav").listen(nav_listener)


