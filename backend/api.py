from flask import Flask, request, jsonify
from flask_restful import Api, Resource, marshal_with, fields, reqparse
from database import Venue, Show, Member, Booking
from database import db
import os
from werkzeug.exceptions import HTTPException
from flask import make_response
from datetime import datetime as dt
import datetime
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity, JWTManager
from flask_bcrypt import Bcrypt
app = Flask(__name__)
api = (Api(app))
import json
from flask import current_app as app
bcrypt = Bcrypt()

class NotFoundError(HTTPException):
    def __init__(self):
        self.response = make_response('The requested resource was not found!',404)

class AlreadyExistsError(HTTPException):
    def __init__(self):
        self.response = make_response('Resource already exists!',409)




#############API for Venue###########################
venue_output_fields = {
    'ID': fields.String,     
    'Name': fields.String,
    'Place': fields.String,
    'Capacity': fields.String
}

venue_parser = reqparse.RequestParser()
venue_parser.add_argument('admin_email')
venue_parser.add_argument('venue_name')
venue_parser.add_argument('venue_place')
venue_parser.add_argument('venue_capacity')

class VenueAPI(Resource):

    # @marshal_with(venue_output_fields)
    @jwt_required()
    def post(self):
        data = request.json
        print(data)
        admin = get_jwt_identity()
        check = Member.query.filter_by(email_ID=admin).first()
        if check.Designation == 'admin':
            name = data['Name']
            place = data['Place']
            capacity = data['Capacity']
            #checking if venue with same name, place, capacity already exists
            venue=Venue.query.filter_by(Admin=admin,
                                Place=place, Name=name, Capacity=capacity).first()
            if not venue:
                new_venue = Venue(Admin=admin,
                                Place=place, Name=name, Capacity=capacity)
                db.session.add(new_venue)
                db.session.commit()
                return {'success': True}, 200
            else:
                raise AlreadyExistsError
        else:
            return {"error":"Access Denied"}
        


    @marshal_with(venue_output_fields)
    @jwt_required()
    def get(self):
        print('called')
        email = get_jwt_identity()
        # email = 'tryuuii@gmail.com'
        print(email) 
        user = Member.query.filter_by(email_ID = email).first()
        if user.Designation == 'admin':
            venue=Venue.query.filter_by(Admin=email).all()
        else:
            venue = Venue.query.all()
        print(venue)
        if venue is not None:
            return venue 
        else:
            raise NotFoundError

    # @marshal_with(venue_output_fields)
    @jwt_required()
    def put(self):
        admin = get_jwt_identity()
        check = Member.query.filter_by(email_ID=admin).first()
        if check.Designation == 'admin':
            data = request.json
            print(data)
            v_id = data['venue_id'] 
            name = data['Name']
            place = data['Place']
            capacity = data['Capacity']
            venue = Venue.query.get(v_id)
            if venue:
                venue.Name = name
                venue.Place = place
                venue.Capacity = capacity
                db.session.commit()
                return {'success': True}, 200

            else:
                raise NotFoundError
        else:
            return {"error":"Access Denied"}
    @jwt_required()
    def delete(self,venue_id):
        admin = get_jwt_identity()
        check = Member.query.filter_by(email_ID=admin).first()
        if check.Designation == 'admin':
            venue=Venue.query.get(venue_id)
            if venue:
                db.session.delete(venue)
                db.session.commit()
                return {'success': True}, 200
            else:
                raise NotFoundError
        else:
            return {"error":"Access Denied"}
        
   


#################API for Show#########################

show_output_fields = {
        'ID' :fields.Integer,
        'Name' :fields.String,
        'Rating' :fields.Integer,
        'Tags' :fields.String,
        'Time' :fields.String,
        'Ticket_Price' :fields.String,
        'V_ID':fields.String,
        'Booked_tickets': fields.Integer,
        'capacity':fields.Integer,
        'venue_name':fields.String

    }

# show_parser = reqparse.RequestParser()
# show_parser.add_argument('show_name')
# show_parser.add_argument('show_rating')
# show_parser.add_argument('show_tags')
# show_parser.add_argument('show_time')
# show_parser.add_argument('show_ticketprice')
# show_parser.add_argument('show_VID')
# show_parser.add_argument('show_bt')
class SearchAPI(Resource):
    @marshal_with(show_output_fields)
    def post(self):
        data = request.json
        search = data['searchstring']
        shows = Show.query.filter(
                Show.Name.ilike('%'+search+'%')).all()
        return shows

class ShowAPI(Resource):
    # @marshal_with(show_output_fields)
    @jwt_required()
    def post(self):
        admin = get_jwt_identity()
        check = Member.query.filter_by(email_ID=admin).first()
        if check.Designation == 'admin':
            data = request.json
            print(data)
            s_name = data['Name'] 
            s_rating = data['Rating']
            s_time = data['Time']
            s_tags = data['Tags']
            s_ticketprice = data['Ticket_Price']
            s_VID = data['venueid']
            s_bt = 0
            # checking if show with same name, rating, tags, time, ticketprice already exists
            show = Show.query.filter_by(Name=s_name, Rating=s_rating,Time=s_time,
                                Tags=s_tags, Ticket_Price=s_ticketprice, V_ID=s_VID).first()
            
            if not show:
                new_show = Show(Name=s_name, Rating=s_rating,Time=s_time,
                                Tags=s_tags, Ticket_Price=s_ticketprice,V_ID=s_VID, Booked_tickets=s_bt)
                db.session.add(new_show)
                db.session.commit()
                return {'success': True}, 200 
            else:
                raise AlreadyExistsError
        else:
            return {"error":"Access Denied"}

    
    @marshal_with(show_output_fields)
    @jwt_required()
    def get(self, venueid=0,showid=0):
        print(venueid,showid)
        showid = int(showid)
        venueid = int(venueid) 
        if showid == 0:
            shows = Show.query.filter_by(V_ID=venueid).all()
        elif venueid == 0:
            print(showid)
            shows = Show.query.filter_by(ID=showid).one()
            venue = Venue.query.filter_by(ID=shows.V_ID).one()
            shows.capacity = venue.Capacity 
            shows.venue_name = venue.Name 
            print(shows.venue_name)
            return shows
        if shows is not None: 
            # print(show_dict) 
            return shows
        else:
            raise NotFoundError

    # @marshal_with(show_output_fields)
    @jwt_required()
    def put(self):
        admin = get_jwt_identity()
        check = Member.query.filter_by(email_ID=admin).first()
        if check.Designation == 'admin':
            data = request.json
            show_id = data['show_id']
            name = data['Name']
            price = data['Price']
            time = data['Time']
            print(data) 
            show = Show.query.get(show_id)
            if show:
                show.Name = name
                show.Time = time
                show.Ticket_Price = price
                db.session.commit()
                return {'success': True}, 200
            else:
                raise NotFoundError
        else:
            return {"error":"Access Denied"}
    @jwt_required()
    def delete(self,venueid):
        admin = get_jwt_identity()
        check = Member.query.filter_by(email_ID=admin).first()
        if check.Designation == 'admin':
            show=Show.query.get(venueid)
            if show: 
                db.session.delete(show)
                db.session.commit()
                return {'success': True}, 200
            else:
                raise NotFoundError
        else:
            return {"error":"Access Denied"}


###########################API for Member######################

member_output_fields = {
        'email_ID' : fields.String,
        'Name': fields.String,
        'ph_num': fields.String,
        'Password': fields.String,
        'Address': fields.String,
    } 

# member_parser = reqparse.RequestParser()
# # member_parser.add_argument('m_fname')
# member_parser.add_argument('name')
# member_parser.add_argument('email')
# member_parser.add_argument('password')
# member_parser.add_argument('ph_num')
# member_parser.add_argument('address')

class LoginAPI(Resource):
    def post(self):
        data = request.json
        print(data)
        email = data['email'] 
        password = data['password']
        member = Member.query.filter_by(email_ID=email).first()
        print(member)
        if member is None or not bcrypt.check_password_hash(member.Password, password):
            return {'status': False, 'msg': 'User ID or Password is incorrect.'}
       
        else:
            expires = datetime.timedelta(days=7)
            access_token = create_access_token(
                identity=email, expires_delta=expires)
            return {'status': True, 'access_token': access_token,'username':member.Name,'designation':member.Designation}, 200

class MemberAPI(Resource):
    def post(self):
        data = request.json
        name = data['name']
        email = data['email']
        password = data['password']
        ph_num = data['ph_num']
        address = data['address']
        designation=data['designation']  
        # return data
        # #checking if member with same name, email, password, designation, location already exists
        member = Member.query.filter_by(email_ID=email).first()
        if not member:
            hashpassword = bcrypt.generate_password_hash(password)
            new_member = Member(email_ID=email, Name=name, ph_num=ph_num, Address=address,
                            Password=hashpassword, Designation=designation)
            db.session.add(new_member)
            db.session.commit()
            expires = datetime.timedelta(days=7)
            access_token = create_access_token(
                identity=email, expires_delta=expires)
            return {'status': True, 'access_token': access_token,'username':name}, 200
            
            # return jsonify({"successful":"successfully"}), 200
        else:
            raise AlreadyExistsError

    @marshal_with(member_output_fields)
    @jwt_required()
    def get(self):
        email = get_jwt_identity()
        member=Member.query.filter_by(email_ID=email).first() 
        print(member.ph_num) 
        if member is not None:
            return member, 200
        else:
            raise NotFoundError

    # @marshal_with(member_output_fields)
    @jwt_required()
    def put(self):
        data = request.json 
        print(data)     
        email = get_jwt_identity()
        password = data['password']
        ph_num = data['ph_nume']
        address = data['address']
        name = data['name']
        hashpassword = bcrypt.generate_password_hash(password)
        member = Member.query.filter_by(email_ID = email).first()
        if member:
            member.Name = name
            member.ph_num = ph_num
            member.Password = hashpassword
            member.Address = address
            db.session.commit()
            return {'status': True}

        else:
            raise NotFoundError

    # def delete(self,member_email):
    #     member=Member.query.get(member_email)
    #     f_name=member.First_name
    #     if member:
    #         db.session.delete(member)
    #         db.session.commit()
    #         return f'{f_name}\'s account has been deleted', 200
    #     else:
    #         raise NotFoundError


###############################API for Booking###########################################################

booking_output_fields = {
        'Booking_ID' : fields.Integer,
        'Show_ID': fields.Integer,
        'User_email': fields.String,
        'Price': fields.Integer,
        'Number_of_Tickets': fields.Integer,
    } 

booking_parser = reqparse.RequestParser()
booking_parser.add_argument('b_ID')
booking_parser.add_argument('b_sID')
booking_parser.add_argument('b_uemail')
booking_parser.add_argument('b_price')
booking_parser.add_argument('b_ticketnum')




class BookingAPI(Resource):
    # @marshal_with(booking_output_fields)
    @jwt_required()
    def post(self):
        data = request.json
        print(data)
        show_id = data['Show_ID']
        email = get_jwt_identity()
        # email = 'tryudfi@gmail.com' 
        price = data['Price']
        ticketnum = data['Number_of_Tickets']
        #checking if booking with same details already exists
        booking = Booking.query.filter_by( Show_ID=show_id, User_email=email,
                            Price=price, Number_of_Tickets=ticketnum).first()
        
        if not booking:
            new_booking = Booking(Show_ID=show_id, User_email=email,
                            Price=price, Number_of_Tickets=ticketnum)
            db.session.add(new_booking)
            db.session.commit()
            return {'status': True}

        else:
            raise AlreadyExistsError


    @marshal_with(booking_output_fields)
    @jwt_required()
    def get(self):
        email = get_jwt_identity()
        booking=Booking.query.filter_by(User_email = email).all()
        if booking is not None:
            return booking, 200
        else:
            raise NotFoundError


    @marshal_with(booking_output_fields)
    def put(self,booking_id):
        args = booking_parser.parse_args()
        booking = Booking.query.get(booking_id)
        if booking:
            booking.Booking_ID = args.get('b_ID')
            booking.Show_ID = args.get('b_sID')
            booking.User_email = args.get('b_uemail')
            booking.Price = args.get('b_price')
            booking.Number_of_Tickets =  args.get('b_ticketnum')
            db.session.commit()
            return booking, 200
        else:
            raise NotFoundError

    def delete(self,booking_id):
        booking=Booking.query.get(booking_id)
        if booking:
            db.session.delete(booking)
            db.session.commit()
            return f'show {booking_id} deleted', 200
        else:
            raise NotFoundError










    