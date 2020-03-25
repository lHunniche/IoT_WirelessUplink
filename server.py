from flask import Flask, request, jsonify, make_response
import time


app = Flask(__name__)

@app.route("/", methods=["POST"])
def index():
    body = request.get_json()
    temp = body.get("temp")
    light = body.get("light")
    trans_id = body.get("count")

    log_file = open("logfile.csv", "a")
    file_output = temp + "," + light + "," + trans_id + "," + str(time.time()) + "\n"
    log_file.write(file_output)
    log_file.close()
    web_output = "Temp: " + temp + "\n" + "Light: " + light + "\n" + "Transmission ID: " + trans_id
    return web_output



if __name__ == "__main__":
    log_file = open("logfile.csv", "w")
    log_file.write("temp,light,trans_id\n")
    log_file.close()
    app.run(debug=True, host='0.0.0.0', port=8080, threaded=True)