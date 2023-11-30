import os
from api import BookingAPI, LoginAPI, MemberAPI, SearchAPI, ShowAPI, VenueAPI
from database import db
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_login import (LoginManager)
from flask_restful import Api
login_manager = LoginManager()
from celery_config import create_celery_inst
from flask import jsonify
from cache_config import make_cache
os.curdir
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = "sqlite:///database.sqlite3"
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI 
app.config["SECRET_KEY"] = 'queen'


db.init_app(app)
api=Api(app)
# bcrypt.init_app(app)
CORS(app)
app.app_context().push()
celery = create_celery_inst(app)
app.app_context().push()
jwt = JWTManager(app)

cache = make_cache(app)
app.app_context().push()
# api.add_resource(MemberAPI, '/api/member')
api.add_resource(MemberAPI,'/api/member','/api/member/<string:user_id>')
api.add_resource(LoginAPI,'/api/login')
api.add_resource(SearchAPI,'/api/search')
api.add_resource(VenueAPI,'/api/add_venue','/api/add_venue/<string:venue_id>')
api.add_resource(BookingAPI,'/api/book_show','/api/book_show/<string:booking_id>')
api.add_resource(ShowAPI,'/api/shows','/api/shows/<string:venueid>','/api/shows/<string:venueid>/<string:showid>')
import celery_task 
@app.route('/venue_report/<int:v_id>')
def venue_report(v_id):
    celery_task.ex_report.delay(v_id)
    return jsonify('Task submitted')

with app.app_context():
    db.create_all()
if __name__ == "__main__":
    app.run(debug=True,port=8000)

# celery -A celery_task.celery worker -l info -B