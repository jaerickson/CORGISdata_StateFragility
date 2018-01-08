from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

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
def get_xyvalues():
	with open('state_fragility (1).json') as demographics_data:
		countries = json.load(demographics_data)
	xyvalues = ""
	d = []
	s = []
	for v in countries:
		if not v["Country"] in s:
			s.append(v["Country"])
			d.append(v["Metrics"]["Legitimacy"]["Legitimacy Score"])
			#print(str(v["Country"]).replace("'","&q'")
			xyvalues += Markup("{ x:'" + str(v["Country"]).replace("'","&quot") +"', y:" + str(v["Metrics"]["Legitimacy"]["Legitimacy Score"])  + "},")
	return xyvalues[0:-1]

def get_legitimacy_score(options):
	with open('state_fragility (1).json') as demographics_data:
		countries = json.load(demographics_data)
	for c in countries:
		if c["Country"] == options:
			legscore = c["Metrics"]["Legitimacy"]["Legitimacy Score"]
	return "Legitimacy Score: " + str(legscore)
	
def get_plegitimacy_score(options):
	with open('state_fragility (1).json') as demographics_data:
		countries = json.load(demographics_data)
	for c in countries:
		if c["Country"] == options:
			plegscore = c["Metrics"]["Legitimacy"]["Political Legitimacy"]
	return "Political Legitimacy: " + str(plegscore)
def get_elegitimacy_score(options):
	with open('state_fragility (1).json') as demographics_data:
		countries = json.load(demographics_data)
	for c in countries:
		if c["Country"] == options:
			elegscore = c["Metrics"]["Legitimacy"]["Economic Legitimacy"]
	return "Economic Legitimacy: " + str(elegscore)
def get_selegitimacy_score(options):
	with open('state_fragility (1).json') as demographics_data:
		countries = json.load(demographics_data)
	for c in countries:
		if c["Country"] == options:
			selegscore = c["Metrics"]["Legitimacy"]["Security Legitimacy"]
	return "Security Legitimacy: " + str(selegscore)
def get_solegitimacy_score(options):
	with open('state_fragility (1).json') as demographics_data:
		countries = json.load(demographics_data)
	for c in countries:
		if c["Country"] == options:
			solegscore = c["Metrics"]["Legitimacy"]["Social Legitimacy"]
	return "Social Legitimacy: " + str(solegscore)
	
def get_peffectiveness_score(options):
	with open('state_fragility (1).json') as demographics_data:
		countries = json.load(demographics_data)
	for c in countries:
		if c["Country"] == options:
			peffscore = c["Metrics"]["Effectiveness"]["Political Effectiveness"]
	return "Political Effectiveness: " + str(peffscore)
def get_eeffectiveness_score(options):
	with open('state_fragility (1).json') as demographics_data:
		countries = json.load(demographics_data)
	for c in countries:
		if c["Country"] == options:
			eeffscore = c["Metrics"]["Effectiveness"]["Economic Effectiveness"]
	return "Economic Effectiveness: " + str(eeffscore)
def get_seeffectiveness_score(options):
	with open('state_fragility (1).json') as demographics_data:
		countries = json.load(demographics_data)
	for c in countries:
		if c["Country"] == options:
			seeffscore = c["Metrics"]["Effectiveness"]["Security Effectiveness"]
	return "Security Effectiveness: " + str(seeffscore)
def get_soeffectiveness_score(options):
	with open('state_fragility (1).json') as demographics_data:
		countries = json.load(demographics_data)
	for c in countries:
		if c["Country"] == options:
			soeffscore = c["Metrics"]["Effectiveness"]["Social Effectiveness"]
	return "Social Effectiveness: " + str(soeffscore)
def get_effectiveness_score(options):
	with open('state_fragility (1).json') as demographics_data:
		countries = json.load(demographics_data)
	for c in countries:
		if c["Country"] == options:
			effscore = c["Metrics"]["Effectiveness"]["Effectiveness Score"]
	return "Effectiveness Score: " + str(effscore)


@app.route("/")
def render_home():
    return render_template('index.html')
@app.route("/l")
def render_legitimacy():
	if "countries" in request.args:
		return render_template('legitimacy.html',countries=get_country_options(),legitimacyscore=get_legitimacy_score(request.args["countries"]),plegitscore=get_plegitimacy_score(request.args["countries"]),
		elegitscore=get_elegitimacy_score(request.args["countries"]),selegitscore=get_selegitimacy_score(request.args["countries"]),solegitscore=get_solegitimacy_score(request.args["countries"]))
	else:
		return render_template('legitimacy.html',countries=get_country_options())
@app.route("/e")
def render_effectiveness():
	if "countries" in request.args:
		return render_template('effectiveness.html',countries=get_country_options(),effectivenessscore=get_effectiveness_score(request.args["countries"]),peffscore=get_peffectiveness_score(request.args["countries"]),
		eeffscore=get_eeffectiveness_score(request.args["countries"]),seeffscore=get_seeffectiveness_score(request.args["countries"]),soeffscore=get_soeffectiveness_score(request.args["countries"]))
	else:
		return render_template('effectiveness.html',countries=get_country_options())
@app.route("/d")
def render_graph():
    return render_template('dotplot.html',datapoints=get_xyvalues())
if __name__ == '__main__':
    app.run(debug=True)
