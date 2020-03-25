from flask import Flask, request, jsonify, make_response
import time


app = Flask(__name__)

@app.route("/", methods=["POST"])
def index():
    body = request.get_json()
    temp_c = body.get("temp_c")
    temp_raw = body.get("temp_raw")
    temp_mv = body.get("temp_mv")
    light = body.get("light")
    trans_id = body.get("count")

    log_file = open("logfile.csv", "a")
    file_output = str(temp_raw) + "," + str(temp_mv) + "," + str(temp_c) + "," + str(light) + "," + str(trans_id) + "," + str(time.time()) + "\n"
    log_file.write(file_output)
    log_file.close()

    return "Jep"



if __name__ == "__main__":
    log_file = open("logfile.csv", "w")
    log_file.write("temp_raw,temp_mv,temp_c,light,trans_id,time\n")
    log_file.close()
    app.run(debug=True, host='0.0.0.0', port=8080, threaded=True)