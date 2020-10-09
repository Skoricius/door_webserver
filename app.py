from flask import Flask, render_template, redirect, url_for, jsonify
import RPi.GPIO as GPIO
import time

class ButtonSwitcher(Flask):
    def __init__(self, port, name):
        super().__init__(name)
        self.port = port
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(port, GPIO.OUT)
        # keep it low by default
        GPIO.output(port, GPIO.LOW)

    def switch_output(self):
        GPIO.output(self.port, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(self.port, GPIO.LOW)
        
        
app = ButtonSwitcher(15, __name__)
    
#@app.route("/")
#@app.route('/home')
#def home():
#    return render_template("button.html", state='Gate button')
	
@app.route('/')
@app.route('/home')
def garage2():
    return render_template("garage2.html", state='ToAddLater')

@app.route("/echo")
def echo():
    print('echo received')
    #app.switch_output()
    return redirect(url_for('home'))
	
@app.route("/trigger")
def trigger():
    app.switch_output()
    msg = {"msg": "Successfully triggered garage door."}
    return jsonify(msg)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=2525)
