from flask import Blueprint
from controllers.user_controller import create_user,getUser,getUsersList,updateUser,login,fetchMyProfile
from flask import request, jsonify
from validators.userValidators import viewUser,CreateUserSchema,EditUserSchema,loginSchema
from middleware.isUserAuth import jwt_middleware

user_bp = Blueprint('user', __name__)

@user_bp.route('/create_user', methods=['POST'])
def create_user_route():
    user_schema = CreateUserSchema()
    errors = user_schema.validate(request.get_json())
    if errors:
        return jsonify(errors)
    return create_user()

@user_bp.route('/view-user',methods=['GET'])
def view_user():
    user_schema = viewUser()
    errors = user_schema.validate(request.args)
    if errors:
        return jsonify(errors)
    return getUser()

@user_bp.route('/list-user',methods=['GET'])
def list_user():
    return getUsersList()

@user_bp.route('/update-user',methods=['POST'])
def update_user():
    user_schema = EditUserSchema()
    errors = user_schema.validate(request.get_json())
    if errors:
        return jsonify(errors)
    return updateUser()

@user_bp.route('/login',methods=['POST'])
def loginUser():
    user_schema = loginSchema()
    errors = user_schema.validate(request.get_json())
    if errors:
        return jsonify(errors)
    return login()

@user_bp.route('/fetch-my-profiles', methods=['GET'])
@jwt_middleware
def fetch_my_profiles(current_user):
    return fetchMyProfile(current_user)