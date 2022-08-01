from flask import Flask, render_template, flash
import os
from forms import EconomicImpactForm


# Configure application
app = Flask(__name__)

# Set secret key
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

# Default homepage


@app.route("/", methods=['GET'])
def index():
    # Get form object
    form = EconomicImpactForm()
    return render_template("index.html", form=form)


@app.route("/", methods=['POST'])
# Calculator function
def calculator():

    # Get form object
    form = EconomicImpactForm()

    if form.validate_on_submit:
        # Get data from the form
        rewards_budget = form.rewards_budget.data
        colu_fee = form.colu_fee.data
        population = form.population.data
        tax_rate = form.tax_rate.data
        third_party_budget = form.third_party_budget.data
        percentage_back = form.percentage_back.data

        
        try:
            # Calculate impact
            inital_economic_impact = round(((rewards_budget + third_party_budget)/percentage_back) + rewards_budget + third_party_budget)
            secondary_local_spending = round(inital_economic_impact * 0.45)
            total_economic_impact = round(inital_economic_impact + secondary_local_spending)
            additional_tax = round(total_economic_impact * tax_rate)
            economic_multiplier = round(total_economic_impact / (rewards_budget + third_party_budget))

            # Render template
            return render_template("index.html", form=form, initial_economic_impact=inital_economic_impact, secondary_local_spending=secondary_local_spending, total_economic_impact=total_economic_impact, additional_tax=additional_tax, economic_multiplier=economic_multiplier)

        except ZeroDivisionError:
            return render_template("index.html", form=form, error="You cannot divide by zero", calculation_success=False)

        except ValueError:
            return render_template("index.html", form=form, error="Cannot perform numerical operations with provided input", calculation_success=False)

        except TypeError:
            return render_template("index.html", form=form, error="Check your input for correct formatting", calculation_success=False)


    else:
        flash("Input data is invalid. Please try again...")
        return render_template("index.html", form=form)
