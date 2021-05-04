from flask import Flask, jsonify, request 
import os 
app = Flask(__name__)
import os
import requests
cf_port = os.getenv("PORT")




@app.route("/", methods=["GET", "POST"])
def home():
	headers={ "X-API-KEY": "3sjOr2rmM52GzhpMHjDEE1kpQeRxwFDr4YcBEimi" }
	response =requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=601201&date=03-05-2021")
	return (str(response.content))

if __name__ == "__main__":
	if cf_port is None:
		app.run( host='0.0.0.0', port=5000, debug=True )
	else:
		app.run( host='0.0.0.0', port=int(cf_port), debug=True )