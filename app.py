from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import subprocess
import datetime
import asyncio


app = Flask(__name__)

# created with the command 'python -c 'import secrets; print(secrets.token_hex())' as suggested by Flask documentation
app.secret_key = b'95cfea064e940d1f09e3bd12b82eaa95a3cf59796af5cead02bba7686cd7249c'

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://<username>:<password>@<server>:5432/<db_name>"
db = SQLAlchemy(app)

# async def formGet():
#     variableNames = ["guests", "rooms", "checkin", "checkout", "bathrooms", "budget", "favouriteStr", "entireHomeStr", "frequency", "email"]
#     tasks = [str(request.form.get(var)) for var in variableNames]
#     results = await asyncio.gather(*tasks)
#     actualResults = []
#     for result in results:
#         actual = await result
#         print("Awaiting task...")
#         actualResults.append(actual)
#     return actualResults

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':        
        checkin = str(request.form['checkin'])
        checkout = str(request.form['checkout'])
        guests = str(request.form['guests'])
        rooms = str(request.form['rooms'])
        bathrooms = str(request.form['bathrooms'])
        budget = str(request.form['budget'])
        favouriteStr = str(request.form['favourite'])
        entireHomeStr = str(request.form['entire'])
        frequency = str(request.form['frequency'])
        email = str(request.form['email'])
        session['formInput'] = [email, checkin, checkout, guests, rooms, bathrooms, budget, favouriteStr, entireHomeStr, frequency]

        # cmd = [
        #     'python',
        #     '/Users/chanc/Documents/2024/OktoberfestAccomodation/main.py',
        #     guests,
        #     rooms,
        #     checkin,
        #     checkout,
        #     budget,
        #     bathrooms,
        #     favouriteStr,
        #     entireHomeStr,
        #     frequency,
        #     email
        # ]

        try:
            # subprocess.run(cmd, check=True, capture_output=True)
            return redirect(url_for('thanks'))
        except subprocess.CalledProcessError as e:
            return "Error executing code: " + str(e)
    else:
        return render_template('index.html')

@app.route('/thanks')
def thanks():
    formInput = session['formInput']
    return render_template('thanks.html', formIn=formInput)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
if __name__ == '__main__':
    app.run(debug=True)