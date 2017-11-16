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
@app.route("/")
def render_home():   
    return render_template('legitimacy.html',countries=get_country_options())
if __name__ == '__main__':
    app.run(debug=False, port=54321)
