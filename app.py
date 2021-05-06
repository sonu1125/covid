from flask import Flask, jsonify, request 
import os 
app = Flask(__name__)
import os
import requests
cf_port = os.getenv("PORT")
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}



@app.route("/", methods=["GET", "POST"])
def home():
	response =requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=601201&date=03-05-2021",headers=headers)
	return (str(response.content))


@app.route('/test2', methods=["GET", "POST"]) 
def test2():
	PINCODE = request.args.get('answer')
	DATE = request.args.get('answer2')
	url='https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=' + PINCODE + '&date=' + DATE
	print(url)
	response = requests.get(url)
	return (response.content)

if __name__ == "__main__":
	if cf_port is None:
		app.run( host='0.0.0.0', port=5000, debug=True )
	else:
		app.run( host='0.0.0.0', port=int(cf_port), debug=True )