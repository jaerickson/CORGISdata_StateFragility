from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__)

def get_state_options():
    with open('county_demographics.json') as demographics_data:
  counties = json.load(demographics_data)
    options = ""
    s = []
    for c in counties:
        if not c["State"] in s:
            s.append(c["State"])
            options += Markup("<option value=\"" + c["State"] + "\">" + c["State"] + "</option>")
    return options
def state_fun_fact(states):
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    s = counties[0]["State"]
    d = counties[0]["County"]
    
    for c in counties:
        if c["State"] == states:
            most_women_owned = counties[0]["Employment"]["Firms"]["Women-Owned"]
            if c["Employment"]["Firms"]["Women-Owned"] > most_women_owned:
                most_women_owned = c["Employment"]["Firms"]["Women-Owned"]
                s = c["State"]
                d = c["County"]
    return d +" is the highest percentage women owned of "+ s +" "+ str(most_women_owned) +"% women owned"
@app.route("/")
def render_home():   
    return render_template('home.html',states=get_state_options())
    return render_template('home.html',fact=state_fun_fact(request.args(get_state_options())))
if __name__ == '__main__':
    app.run(debug=False, port=54321)
