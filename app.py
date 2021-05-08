from flask import Flask, jsonify, request 
import os 
app = Flask(__name__)
import os
import requests
cf_port = os.getenv("PORT")
content_type = 'application/json' 
headers = {'Content-Type': content_type}


@app.route("/", methods=["GET", "POST"])
def home():
	response =requests.get("https://api.covidbedsindia.in/v1/storages/608982f703eef3de2bd05a72/Bengaluru",verify=False)
	return (str(response.content))


@app.route('/test2', methods=["GET", "POST"]) 
def test2():
	PINCODE = request.args.get('answer')
	DATE = request.args.get('answer2')
	url='https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=' + PINCODE + '&date=' + DATE
	print(url)
	response = requests.get(url,headers=headers)
	return (response.content)

@app.route('/test3') 
def test3():
	return ('hello')

if __name__ == "__main__":
	if cf_port is None:
		app.run( host='0.0.0.0', port=5000, debug=True )
	else:
		app.run( host='0.0.0.0', port=int(cf_port), debug=True )