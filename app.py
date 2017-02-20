from flask import Flask, request, flash, url_for, redirect, render_template
# import RPi.GPIO as GPIO
import datetime

app = Flask(__name__)

@app.route('/')
def login():
      return render_template('login.html')

@app.route('/dashboard')
def dashboard():
      return render_template('dashboard.html')

@app.route('/register', methods = ['GET', 'POST'])
def register():
      return render_template('register.html')

@app.route('/light', methods = ['GET', 'POST'])
def light():
      if request.method == "POST":
            device_name = request.form['device']
            state = request.form['state']
            # GPIO.setmode(GPIO.BCM)
            # GPIO.setup(2, GPIO.OUT)
            # GPIO.output(2, True)
            return render_template('light.html', device_name = device_name, state = state)
      else:
            return render_template('light.html')

if __name__ == '__main__':
   app.run(host='0.0.0.0', debug = True)
