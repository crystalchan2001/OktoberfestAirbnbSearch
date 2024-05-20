from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import subprocess
import datetime
import asyncio


app = Flask(__name__)

async def formGet():
    variableNames = ["guests", "rooms", "checkin", "checkout", "bathrooms", "budget", "favouriteStr", "entireHomeStr", "frequency", "email"]
    tasks = [str(request.form.get(var)) for var in variableNames]
    results = await asyncio.gather(*tasks)
    actualResults = []
    for result in results:
        actual = await result
        print("Awaiting task...")
        actualResults.append(actual)
    return actualResults

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':        
        timeStart = datetime.datetime.now()
        try:
            vars = asyncio.run(formGet())
            print("[VARS] " + str(vars))
        except:
            print("THERE WAS AN ERROR")
        # checkin = str(request.form.get('checkin'))
        # checkout = str(request.form.get('checkout'))
        # guests = str(request.form.get('guests'))
        # rooms = str(request.form.get('rooms'))
        # bathrooms = str(request.form.get('bathrooms'))
        # budget = str(request.form.get('budget'))
        # favouriteStr = str(request.form.get('favourite'))
        # entireHomeStr = str(request.form.get('entire'))
        # frequency = str(request.form.get('frequency'))
        # email = str(request.form.get('email'))

        timeEnd = datetime.datetime.now()
        timeTaken = timeEnd - timeStart
        print(f"[TIME TAKEN] {timeTaken}")
        
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
        # cmd = [
        #     'python',
        #     '/Users/chanc/Documents/2024/OktoberfestAccomodation/main.py',
        #     vars[0],
        #     vars[1],
        #     vars[2],
        #     vars[3],
        #     vars[4],
        #     vars[5],
        #     vars[6],
        #     vars[7],
        #     vars[8],
        #     vars[9]
        # ]

        # print(f"[CALLING CMDLINE] {cmd}")

        try:
            # subprocess.run(cmd, check=True, capture_output=True)
            return redirect(url_for('thanks'))
        except subprocess.CalledProcessError as e:
            return "Error executing code: " + str(e)
        
    return render_template('index.html')

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

if __name__ == '__main__':
    app.run(debug=True)