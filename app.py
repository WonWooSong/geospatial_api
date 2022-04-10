from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)

class House(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  type = db.Column(db.String(120), unique=False, nullable=False)
  latitude = db.Column(db.Float, unique=False, nullable=False)
  longitude = db.Column(db.Float, unique=False, nullable=False)
  address = db.Column(db.String(250), unique=False, nullable=False)
  bed_num = db.Column(db.Integer, unique=False, nullable=False)
  bath_num = db.Column(db.Integer, unique=False, nullable=False)

  def __init__(self, type, latitude, longitude, address, bed_num, bath_num):
    self.type = type
    self.latitude = latitude
    self.longitude = longitude
    self.address = address
    self.bed_num = bed_num
    self.bath_num = bath_num

db.create_all()

@app.route('/')
def get_root():
    print('sending docs')
    return render_template('swaggerui.html')

@app.route('/house', methods=['POST'])
def create_location():
  body = request.get_json()

  db.session.add(House(body['geometry']['type'], body['geometry']['latitude'], body['geometry']['longitude'], body['address'], body['bed'], body['bath']))
  db.session.commit()
  return "Realestate house information created."

@app.route('/house', methods=['GET'])
def get_locations():
  response = []
  for house in db.session.query(House).all():
    del house.__dict__['_sa_instance_state']
    location_id = house.id
    address = house.address
    response_entry = {
      'type':house.type,
      'latitude': house.latitude,
      'longitude': house.longitude
    }
    bed = house.bed_num
    bath = house.bath_num
    response_entry = {'id':location_id, 'geometry':response_entry, 'address':address, 'bed':bed, 'bath':bath}
    response.append(response_entry)
    
  return jsonify(response)