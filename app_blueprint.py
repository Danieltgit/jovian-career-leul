from flask import Blueprint, render_template

JOBS = [{
  "id": 1,
  "title": "Data Scientist",
  "location": "Hawassa, Ethiopia",
  "salary": "$12,000"
}, {
  "id": 2,
  "title": "Data Analysit",
  "location": "Addis Ababa, Ethiopia",
  "salary": "$22,000"
}, {
  "id": 3,
  "title": "Database Engineer",
  "location": "Mekele, Ethiopia",
  "salary": "$27,000"
}]

app_blueprint = Blueprint('app_blueprint', __name__)


@app_blueprint.route("/")
def index():
   return render_template('home.html',
    jobs=JOBS,
    company_name="High-Tech IT Solutions",
  )

@app_blueprint.route("/about")
def about():
  return render_template('about.html')

