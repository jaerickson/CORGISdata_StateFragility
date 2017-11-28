from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__)

def get_country_options():
    with open('state_fragility (1).json') as demographics_data:
        countries = json.load(demographics_data)
    options = ""
    s = []
    for c in countries:
        if not c["Country"] in s:
            s.append(c["Country"])
            options += Markup("<option value=\"" + c["Country"] + "\">" + c["Country"] + "</option>")
    return options

def get_legitimacy_score(options):
	with open('state_fragility (1).json') as demographics_data:
		countries = json.load(demographics_data)
	for c in counrties:
		if c["Country"] == options:
			if(type=="submit"):
				legscore = c
			else:
				legscore = " "
	return legscore

@app.route("/")
def render_main():
    return render_template('index.html')
@app.route("/l")
def render_legitimacy():
    #return render_template('legitimacy.html',countries=get_country_options(),legislativescore=get_legitimacy_score(request.args["countries"]))
	return render_template('legitimacy.html',countries=get_country_options(),legitimacyscore=str("score"))
@app.route("/e")
def render_effectiveness():   
    return render_template('effectiveness.html',countries=get_country_options())
if __name__ == '__main__':
    app.run(debug=True, port=54321)
