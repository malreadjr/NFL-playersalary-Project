# import necessary libraries
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

from flask_sqlalchemy import SQLAlchemy
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///nflDB.db"

#  os.environ.get('DATABASE_URL', '') or 

# Remove tracking modifications
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

engine = create_engine("sqlite:///nflDB.db")

Base = automap_base()

Base.prepare(engine, reflect=True)

Positions = Base.classes.positions

# results = session.query(Positions.position, Positions.offenseDefense).all()

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")



@app.route("/api/salaries")
def salaries():

    session = Session(engine)

    results = session.query(Positions.position, Positions.offenseDefense).all()
    

    # hover_text = [result[1] for result in results]
    # year = [result[0] for result in results]
    # salary = [result[1] for result in results]

    position_data = []

    for position, ofdf in results:
        pos_dict = {}
        pos_dict['position'] = position
        pos_dict['offenseDefense'] = ofdf
        position_data.append(pos_dict)

    return jsonify(position_data)


if __name__ == "__main__":
    app.run()
