from flask import Flask , render_template 
import random
app = Flask (__name__)

@app.route("/")
def load_page  ():	
	return render_template("fashion_page1.html")
@app.route("/dresses")
def dresses  ():	
	#return render_template("dresses.html")
	name=["Renan" , "Kawther" , "Roaa"]	
	return render_template ("dresses.html" , name=random.choice(name))

if __name__== "__main__":
	app.run()
