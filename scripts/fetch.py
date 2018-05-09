import pyrebase

config = {
  "apiKey": "AIzaSyBBMTte0i4rrpPb1k0HEAdzzfXNQPOTFhs",
  "authDomain": "nutrition-mis2018.firebaseapp.com",
  "databaseURL": "https://nutrition-mis2018.firebaseio.com",
  "storageBucket": "nutrition-mis2018.appspot.com",
	}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
users_by_value = db.child("test").child("count").get()
x = str(users_by_value.val()+1)
storage = firebase.storage()
storage.child("image/"+x+".jpg").download("0.jpg")
