from flask import Flask , render_template , request 
import random , dataset
app = Flask (__name__)

#db = dataset.connect("postgres://yowahpfaxtsjoc:89e78de430594fa7bffec234ce5bc8ac9193cef0a864378fd900ddd573d65651@ec2-23-23-244-83.compute-1.amazonaws.com:5432/dbn2rcviq5s3i4")
#table = db["bakeza_user"]
#table.insert(dict(name="bakeza Diazada" , age=14 , country= "Gaza" ))
#table.insert(dict(name="Roaa Wadi" , age=14 , country= "Gaza" ))
#print (db.tables)
#print (table.columns)
#user = table.find_one(name="Roaa Wadi")
#print("Id: "+ str(user["id"]) + "; Name :" + user["name"] + str(user["age"]) + user["country"])


@app.route("/")
def load_page  ():	
	return render_template("fashion_page1.html")
@app.route("/dresses")
def dresses  ():	
	return render_template ("dresses.html")

@app.route("/contact")
def cotact():
	 return render_template ("contact.html")
@app.route("/pants")
def pants():
	 return render_template ("pants.html")

@app.route("/t-shirts")
def t_shirts():
	
	 return render_template ("t-shirts.html")
	 
if __name__== "__main__":
	app.run()
