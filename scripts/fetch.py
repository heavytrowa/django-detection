import pyrebase

config = {
  "apiKey": "AIzaSyBBMTte0i4rrpPb1k0HEAdzzfXNQPOTFhs",
  "authDomain": "nutrition-mis2018.firebaseapp.com",
  "databaseURL": "https://nutrition-mis2018.firebaseio.com",
  "storageBucket": "nutrition-mis2018.appspot.com",
	}
firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
storage.child("image/.jpg").download("0.jpg")
