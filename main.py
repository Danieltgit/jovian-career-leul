""" 
this is the first 
python based webased programming 
thuis is my sample personal website
"""
JOBS = [
  {
    "id": 1,
    "title":"Data Scientist",
    "location":"Hawassa, Ethiopia",
    "salary": "$12,000"
  }, 
  {
    "id": 2,
    "title":"Data Analysit",
    "location":"Addis Ababa, Ethiopia",
    "salary": "$22,000"
  }, 
    {
    "id":3,
    "title":"Database Engineer",
    "location":"Mekele, Ethiopia",
    "salary": "$27,000"
  }
]
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
  return render_template('home.html', jobs = JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug = True)