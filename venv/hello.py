from flask import *
from flask_cors import CORS
import json
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/ping", methods=["GET"])
def GET_ping():
	with open("arc.txt", "r") as arc:
		arc_data = json.load(arc)
	return arc_data[::-1]
	
@app.route("/queue", methods=["GET"])
def GET_queue():
	with open("test.txt", "r") as qu:
		qu_data = json.load(qu)
	return qu_data[::-1]

@app.route("/remove", methods=["POST"])
def Post_remove():
	data = request.form.to_dict()
	#print(data)
	
	with open("test.txt", "r") as st:
		st_list = json.load(st)
	
	if data in st_list:
		st_list.remove(data)
		
		with open("test.txt", "w") as st:
			#print(st_list)
			json.dump(st_list, st)
			return "removed"
	
	return "not in queue"

@app.route("/ping", methods=["POST"])
def POST_ping():
	data = request.form.to_dict()
	#print(data, type(data))
	#print("test")
	
	with open("test.txt", "r") as ts:
		ts_data = json.load(ts)
		#print(ts_data, type(ts_data))
	
	pair, ts_data = pair_student(ts_data, data)
	
	with open("test.txt", "w") as ts:
		#print(ts_data)
		json.dump(ts_data, ts)
	return pair

def pair_student(std_list, new_std):
	#print("test")
	for std in std_list:
		if std["drop_cours"] == new_std["take_cours"]:
			if std["take_cours"] == new_std["drop_cours"]:
				#print(std, new_std)
				archive([std, new_std])
				std_list.remove(std)
				return [std, new_std], std_list
	
	std_list.append(new_std)
	return [], std_list

def archive(data):
	time = datetime.now().strftime("%d/%m/%y %H:%M:%S")
	data.append(time)
	with open("arc.txt", "r") as arc:
		arc_data = json.load(arc)
		
	arc_data.append(data)
	
	with open("arc.txt", "w") as arc:
		#print(arc_data)
		json.dump(arc_data, arc)






