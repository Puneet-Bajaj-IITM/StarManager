import pandas as pd
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from flask import Flask, render_template, request, redirect
from datetime import datetime
from utils import fetchCSV, writeCSV

app = Flask(__name__)
df = fetchCSV()
df.index.name = 'ID'




def add_activity(typename, company_id):
    current_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    df.loc[len(df)] = [typename, company_id, 'test user', current_timestamp, None, None]
    writeCSV(df)

def update_activity(activity_id, typename, company_id):  
    data = df.loc[[activity_id]].squeeze()  
    current_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    df.loc[activity_id] = [typename, company_id, data['CreatedBy'] ,data['CreatedOn'] ,current_timestamp, 'test user']
    writeCSV(df)

def delete_activity(activity_id):
    df.drop(activity_id, axis=0, inplace=True)
    writeCSV(df)

app.config['SECRET_KEY'] = 'gaangu'

class ActivityForm(FlaskForm):
    typename = StringField('Type Name')
    company_id = StringField('Company ID')
    submit = SubmitField('Submit')

@app.route("/")
def index():
    return render_template("index.html", dataframe=df, msg="Table Activities")
    
@app.route("/add", methods=["GET", "POST"])
def add():
    form = ActivityForm()
    if request.method == "POST":
        if form:
            typename = form.typename.data
            company_id = form.company_id.data
            add_activity(typename, int(company_id))
            return redirect("/")
    return render_template("add.html", form=form)

@app.route("/update", methods=["GET"])
def update_form():
    activity_id = int(request.args.get('id'))
    data = df.loc[[activity_id]].squeeze()  # Using DataFrame index to filter
    return render_template("update.html", data=data, activity_id=activity_id)


@app.route("/update/<int:activity_id>", methods=["GET", "POST"])
def update(activity_id):
    form = ActivityForm()
    if request.method == "POST":
        if form:
            typename = form.typename.data
            company_id = form.company_id.data
            update_activity(activity_id, typename, int(company_id))
            return redirect("/")
    return render_template("update.html", form=form, activity_id=activity_id)


@app.route("/remove", methods=["GET"])
def delete():
    activity_id = request.args.get('id')
    delete_activity(int(activity_id))   
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
