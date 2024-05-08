from flask import Flask, render_template, request
import os


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        checkin = str(request.form.get('checkin'))
        checkout = str(request.form.get('checkout'))
        guests = str(request.form.get('guests'))
        rooms = str(request.form.get('rooms'))
        bathrooms = str(request.form.get('bathrooms'))
        budget = str(request.form.get('budget'))
        favouriteStr = str(request.form.get('favourite'))
        entireHomeStr = str(request.form.get('entire'))
        frequency = str(request.form.get('frequency'))
        email = str(request.form.get('email'))

        toCall = f"""[PRINTING INPUT] python OktoberfestAccomodation/main.py 
                {guests} {rooms} {checkin} {checkout} {budget} {bathrooms} {favouriteStr} {entireHomeStr} 
                {frequency} {email}"""
        print(toCall)
        # os.system()
        
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)