import json
import uuid
from flask import Flask, request

def generate_uuid():
  unique_id = str(uuid.uuid4())
  return unique_id

app = Flask(__name__)
@app.route("/detect", methods=["post"])
def execute():
  content_type = request.headers.get("Content-Type")
  request_id = generate_uuid()
  return {"statusCode":400, "body": json.dumps({"message":"Invalid Contrnt", "request_id":request_id})}

if __name__ == "__main__":
  app.run(host="0.0.0.0",port=8080,debug=True)
