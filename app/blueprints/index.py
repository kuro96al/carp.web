from flask import Blueprint, render_template
from sqlalchemy import func
from app.models import Sentimental
from app.models import db

app = Blueprint('index', __name__)


@app.route('/', methods=['GET'])
def index():
    sentimentals = [s.to_dict() for s in Sentimental.query.all()]
    totals = db.session\
               .query(Sentimental.sentimental, func.count(Sentimental.id))\
               .group_by(Sentimental.sentimental)\
               .all()
    return render_template('index.html', sentimentals=sentimentals, totals=totals)
