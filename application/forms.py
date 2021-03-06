"""
forms.py

Web forms based on Flask-WTForms

See: http://flask.pocoo.org/docs/patterns/wtforms/
     http://wtforms.simplecodes.com/

"""

import datetime
import pytz

from flask_wtf import FlaskForm
from wtforms import validators, SelectField, TextField, IntegerField, DateTimeField, FloatField, BooleanField
import wtforms.ext.dateutil.fields


class CoffeeForm(FlaskForm):
    person = SelectField("Addict", coerce=int)
    coffee = TextField("Coffee", [validators.Required()])
    price = FloatField("Price", default=0)
    runid = SelectField("Run", coerce=int)


class RunForm(FlaskForm):
    person = SelectField("Person", coerce=int)
    time = wtforms.ext.dateutil.fields.DateTimeField(
            "Time of Run",
            [validators.Required()],
            # Ensure the time has a timezone attached (note numerical format
            # works, the name does not).
            display_format="%Y/%m/%d %H:%M %z")

    cafeid = SelectField("Cafe", coerce=int)
    pickup = TextField("Pickup Location")
    is_open = BooleanField("Currently accepting coffees")


class CafeForm(FlaskForm):
    name = TextField("Name", [validators.Required()])
    location = TextField("Location")


class PriceForm(FlaskForm):
    cafeid = SelectField("Cafe", coerce=int)
    price_key = TextField("Coffee (e.g. large cap)")
    amount = FloatField("Amount", [validators.Required()])
