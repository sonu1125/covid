from flask import Flask, jsonify, request 
import os 
app = Flask(__name__)
import os
import requests
cf_port = os.getenv("PORT")
content_type = 'application/json' 
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

@app.route("/", methods=["GET", "POST"])
def home():
	response =requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=601201&date=03-05-2021",headers=headers)
	return (str(response.content))

@app.route("/blr", methods=["GET", "POST"])
def blr():
	response =requests.get("https://api.covidbedsindia.in/v1/storages/608982f703eef3de2bd05a72/Bengaluru",verify=False)
	return (response.content)



@app.route("/chn", methods=["GET", "POST"])
def chn():
	response =requests.get("https://api.covidbedsindia.in/v1/storages/6089820e03eef3b588d05a6d/Tamil%20Nadu",verify=False)
	return (response.content)



@app.route("/ap", methods=["GET", "POST"])
def ap():
	response =requests.get("https://api.covidbedsindia.in/v1/storages/608982e003eef31f34d05a71/Andhra%20Pradesh",verify=False)
	return (response.content)


@app.route("/hyd", methods=["GET", "POST"])
def hyd():
	response =requests.get("https://api.covidbedsindia.in/v1/storages/6089829403eef36d93d05a6f/Telangana",verify=False)
	return (response.content)

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