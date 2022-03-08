import pprint
import json
from flask import Flask,render_template, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# read config file and load configuration
with open("config/config.json") as config_file:
    service_config = json.load(config_file)

app.config["mongo"] = MongoClient(
    service_config.get("mongo_db_url", "mongodb://172.21.0.2"),
    service_config.get("mongo_db_port", 27017),
)

app.config["version"] = service_config.get("service_version", "ConfigNotLoaded!!")


@app.route("/")
def version():
    return render_template('index.html')

@app.route("/sample", methods=["GET"])
def listSamples():
    myclient=MongoClient("mongodb://172.21.0.2:27017/")
    mydb=myclient["samples"]
    mycol=mydb["samples"]

    data = []
    for sample in mycol.find():
        data.append(
            {
                "sample_id": sample.get("sample_id"),
                "sample_name": sample.get("sample_name"),
                "sample_description": sample.get("sample_description"),
            }
        )
    return jsonify({"samples": data})


@app.route("/sample", methods=["POST"])
def addSample():
    post_data = dict(request.json)
    pprint.pprint(post_data)
    myclient=MongoClient("mongodb://172.21.0.2:27017/")
    mydb=myclient["samples"]
    mycol=mydb["samples"]
    x=mycol.insert_one(post_data)

    return jsonify(success=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
