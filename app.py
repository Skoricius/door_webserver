from flask import Flask, render_template, redirect, url_for, jsonify
import RPi.GPIO as GPIO
import time


class ButtonSwitcher(Flask):
    def __init__(self, port, name):
        super().__init__(name)
        self.port = port
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(port, GPIO.OUT)
        # keep it high by default
        GPIO.output(port, GPIO.HIGH)

    def switch_output(self):
        state = self.get_state()
        if state == 0:
            GPIO.output(self.port, GPIO.HIGH)
        elif state == 1:
            GPIO.output(self.port, GPIO.LOW)

    def get_state(self):
        state = GPIO.input(self.port)
        return state


app = ButtonSwitcher(15, __name__)

# @app.route("/")
# @app.route('/home')
# def home():
#    return render_template("button.html", state='Gate button')


@app.route('/')
@app.route('/home')
def home():
    state = app.get_state()
    print(state)
    if state == 0:
        button_caption = 'Start MOKE'
    elif state == 1:
        button_caption = 'Stop MOKE'
    print(button_caption)
    return render_template("garage2.html", state=button_caption)


@app.route("/echo")
def echo():
    print('echo received')
    app.switch_output()
    return redirect(url_for('home'))


@app.route("/trigger")
def trigger():
    app.switch_output()
    msg = {"msg": "Successfully triggered."}
    return jsonify(msg)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=2525)
