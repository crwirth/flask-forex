from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from forex_python.converter import CurrencyRates
from flask_api import FlaskAPI

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'SjdnUends821Jsdlkvxh391ksdODnejdDw'

c = CurrencyRates()

@app.route('/')
def form():
    return render_template('/index.html', form=form)

@app.route('/', methods=['POST'])
def result():
    parameters = request.form.to_dict()
    params = list(parameters.values())
    params[2:] = [int(l) for l in params[2:]]
    print(params)
    result = c.convert(*params)
    return f"""
    <h1>The result is: {result}  </h1>
   """

if __name__ == "__main__":
    app.run()