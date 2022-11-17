from flask import *
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/ping", methods=["GET"])
def GET_ping():
	return render_template("student_reg.html")

@app.route("/ping", methods=["POST"])
def POST_ping():
	data = request.form.to_dict()
	print(data, type(data))
	
	with open("test.txt", "r") as ts:
		ts_data = json.load(ts)
		print(ts_data, type(ts_data))
	
	ts_data = pair_student(ts_data, data)
	
	with open("test.txt", "w") as ts:
		print(ts_data)
		json.dump(ts_data, ts)
	return "got POST"

def pair_student(std_list, new_std):
	for std in std_list:
		if std["drop_cours"] == new_std["take_cours"]:
			if std["take_cours"] == new_std["drop_cours"]:
				print(std, new_std)
				std_list.remove(std)
				return std_list
	
	std_list.append(new_std)
	return std_list




