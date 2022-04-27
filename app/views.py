from app import app
from app import task
from .scripts import *
from flask import abort, render_template, request, redirect, url_for

@app.route("/")
def index():
	return redirect(url_for("form", method="tabel"))

@app.route("/form/<method>")
def form(method):
	nav_data = task.read_json("app/data/nav.json")
	method_name = task.remove_dash(method)
	return render_template("form.html", nav=nav_data, method=method_name)

@app.route("/result/<method>", methods=["GET", "POST"])
def result(method):
	if request.method == "POST":
		nav_data = task.read_json("app/data/nav.json")
		method_data = task.read_json("app/data/method.json")
		method_name = task.remove_dash(method)
		input_data = {}
		for k, v in method_data[method_name]["input"].items():
			input_data[k] = eval(v)
		calculation_results = eval(method_data[method_name]["function"])
		if len(calculation_results) == 3:
			return render_template(
				"result.html",
				nav=nav_data,
				method=method_name, 
				data=calculation_results[0], 
				tables=[
					calculation_results[1].to_html(
						classes="data",
						header="true",
						index=False
					)
				],
				conclusion=calculation_results[2]
			)
		else:
			return render_template(
				"result.html",
				nav=nav_data,
				method=method_name, 
				data=calculation_results[0], 
				message=calculation_results[1]
			)
	else:
		abort(404)