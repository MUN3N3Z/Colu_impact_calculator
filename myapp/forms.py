"""Form object declaration."""
from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.fields.numeric import IntegerField, FloatField
from wtforms.validators import InputRequired

class EconomicImpactForm(FlaskForm):
        # Data to be collected and displayed on index.html
        rewards_budget = IntegerField("Rewards Budget", [InputRequired(message="Please input your city's reward budget")])
        colu_fee = IntegerField("Colu Fee", [InputRequired(message="Please Colu's service fee")])
        population = IntegerField("Population", [InputRequired(message="Please input your city's population")])
        tax_rate = FloatField("Tax Rate", [InputRequired(message="Please input your city's tax rate")])
        third_party_budget = IntegerField("Third Party Budget", [InputRequired(message="If available, please input a third party's budget. Else input 0")])
        percentage_back = FloatField("Percentage back to shoppers", [InputRequired(message="What percentage would you like to give back to shoppers")]) 
        submit = SubmitField("Submit")
