from config.db import db
from flask import request, jsonify
from models.user import User
from flask_jwt_extended import create_access_token
from datetime import timedelta

def create_user():
    try:
        data = request.get_json()
        print(data,"data")
        new_user = User(
            user_name=data['user_name'],
            phone_number=data['phone_number'],
            email=data['email']
        )
        db.session.add(new_user)
        db.session.commit()

        user_details = {
            "id": new_user.id,
            "user_name": new_user.user_name,
            "phone_number": new_user.phone_number,
            "email": new_user.email
        }

        # Return the user details as part of the response
        response_data = {
            "message": "User created successfully!",
            "user": user_details
        }
        return jsonify(response_data), 200
    except Exception as e:
        db.session.rollback()
        return {"message": "Error creating user", "error": str(e)}, 500  # Use an appropriate status code for errors
    finally:
        db.session.close()


def getUser():
    try:
        id = request.args.get('id')
        user = User.query.get(id)
        if user:
            user_details = {
                "id": user.id,
                "user_name": user.user_name,
                "phone_number": user.phone_number,
                "email": user.email
            }
            response_data = {
                "message": "User Fetched successfully!",
                "user": user_details
            }
            return jsonify(response_data), 200
        else: return {"message": "User not found"}, 400
    except Exception as e:
        db.session.rollback()
        return {"message": "Error fetching user", "error": str(e)}, 500
    finally:
        db.session.close()


def getUsersList():
    try:
        users = User.query.all()
        user_details =[ {
            "id": user.id,
            "user_name": user.user_name,
            "phone_number": user.phone_number,
            "email": user.email
        } for user in users]
        
        response_data = {
            "message": "Users Fetched successfully!",
            "users": user_details
        }
        return jsonify(response_data), 200
    except Exception as e:
        db.session.rollback()
        return {"message": "Error listing user", "error": str(e)}, 500
    finally:
        db.session.close()

def updateUser():
    try:
        data = request.get_json()
        user = User.query.get(data["id"])
        if user:
           user.user_name = data['user_name']
           user.phone_number=data['phone_number']
           user.email = data['email']
           db.session.commit()
           user_details = {
            "id": user.id,
            "user_name": user.user_name,
            "phone_number": user.phone_number,
            "email": user.email
            }
           response_data = {
            "message": "User updated successfully!",
            "user": user_details
            }
           return jsonify(response_data), 200
        else: 
            return {"message": "User not found"}, 400
    except Exception as e:
        db.session.rollback()
        return {"message": "Error listing user", "error": str(e)}, 500
    finally:
        db.session.close()

def login():
    try:
        data = request.get_json()
        user = User.query.filter_by(user_name=data["user_name"]).first()
        if user:
           expires = timedelta(hours=72)
           additional_claims = {
                'user_id': user.id,
                'user_role': 'admin'
            }
           access_token = create_access_token(identity=user.id, expires_delta=expires, additional_claims=additional_claims)
           print("Access Token:", access_token)
           return jsonify(access_token=access_token), 200
        else: 
            return {"message": "User not found"}, 400 
    except Exception as e:
        db.session.rollback()
        return {"message": "Error listing user", "error": str(e)}, 500
    finally:
        db.session.close()

def fetchMyProfile(current_user):
    try:
        user = User.query.get(current_user)
        user_posts = user.posts

        if user:
            user_details = {
                "id": user.id,
                "user_name": user.user_name,
                "phone_number": user.phone_number,
                "email": user.email
            }
            # user_posts_details = [{
            #     "id":user_posts,
            #     # "user_id": user_posts.user_id
            # }for userposts in user_posts]
            response_data = {
                "message": "profile Fetched successfully!",
                "user": user_details,
                # "posts":user_posts_details
            }
            return jsonify(response_data), 200
        else: return {"message": "User not found"}, 400
    except Exception as e:
        db.session.rollback()
        return {"message": "Error listing user", "error": str(e)}, 500 
    finally:
        db.session.close() 