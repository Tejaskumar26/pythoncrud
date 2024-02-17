from marshmallow import Schema, fields, validate


class viewUser(Schema):
    id = fields.String(
        required=True,
        validate=validate.Regexp(
            r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$',
            error="Invalid UUID format"
        ),
        error_messages={"required": "ID parameter is required", "invalid": "ID must be a valid UUID"}
    )

class CreateUserSchema(Schema):
    user_name = fields.String(
        required=True,
        validate=[validate.Length(min=1, error="user_name parameter is required"),],
        error_messages={"required": "user_name parameter is required"}
    )
    phone_number = fields.String(
        required=True,
        validate=[
            validate.Length(min=1, error="Phone number required"),
            validate.Length(equal=10, error="Phone number must be 10 digits"),
            validate.Regexp(r'^\d+$', error="Phone number must consist of digits only")
        ],
        error_messages={"required": "phone_number parameter is required"}
    )
    email = fields.Email(
        required=True,
        error_messages={"required": "email parameter is required", "invalid": "Invalid email format"}
    )

class EditUserSchema(Schema):
    id = fields.String(
        required=True,
        validate=[
            validate.Length(min=1, error="id parameter is required"),
            validate.Regexp(r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$',
            error="Invalid UUID format"
        )]
    )
    user_name = fields.String(
        required=True,
        validate=[validate.Length(min=1, error="user_name parameter is required"),],
        error_messages={"required": "user_name parameter is required"}
    )
    phone_number = fields.String(
        required=True,
        validate=[
            validate.Length(min=1, error="Phone number required"),
            validate.Length(equal=10, error="Phone number must be 10 digits"),
            validate.Regexp(r'^\d+$', error="Phone number must consist of digits only")
        ],
        error_messages={"required": "phone_number parameter is required"}
    )
    email = fields.Email(
        required=True,
        error_messages={"required": "email parameter is required", "invalid": "Invalid email format"}
    )

class loginSchema(Schema):
    user_name = fields.String(
        required=True,
        validate=[validate.Length(min=1, error="user_name parameter is required"),],
        error_messages={"required": "user_name parameter is required"}
    )