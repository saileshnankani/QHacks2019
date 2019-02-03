from flask import Flask
from flask import render_template
from calendar_components import *
from flask import request

app = Flask(__name__)


@app.route('/', methods=["GET"])
def main_calendar_view():
    #DO CODE TO POPULATE CALENDAR
    m = CalendarComponents("Red", "Assignment")

    return render_template("calendar.html") #m1200=new_component.render_component())

@app.route('/add_event', methods=["GET"])
def add_event():
    return render_template("add_event.html")

@app.route('/process_event', methods=["GET", "POST"])
def process_event():
    if request.method == "POST":
        category = request.form["category"]
        date = request.form["date"]
        time = request.form["time"]
        duration = request.form["duration"]
        return str(category) # just to see what select is
    if request.method == "GET":
        print("HELLO")
        return "Fail"



if __name__ == '__main__':
    app.run()
