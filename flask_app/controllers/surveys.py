# burgers.py
from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.survey import Survey





@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def sub_info():

    if not Survey.validate_survey(request.form):
        return redirect("/")

    name_from_form = request.form['name']
    area_from_form = request.form['area']
    languages_from_form = request.form['languages']
    comment_from_form = request.form['comment']
    
    return render_template('result.html',
    name_on_template=name_from_form,
    area_on_template=area_from_form,
    languages_on_template=languages_from_form,
    comment_on_template=comment_from_form)
