from app.models.email import Email
from app.repository.base import get_record_by_field
from app.services.cold_mail import generate_cold_mail
from . import routes_blueprint
from ..error_handler import url_validation_error_handler
from flask_parameter_validation import ValidateParameters, Route
from ..helpers import create_response
from ..constants import SUCCESS_MESSAGE,DUMMY_EMAIL
from ..enums import CustomStatusCode, EmailStatus
from datetime import datetime

@routes_blueprint.route('/emails/generate/<int:prospect_id>', methods=['GET'])
@ValidateParameters(url_validation_error_handler)
def generate_email(prospect_id: int = Route()):
    data = generate_cold_mail(prospect_id)
    return create_response(CustomStatusCode.SUCCESS.value, SUCCESS_MESSAGE, data), 200

@routes_blueprint.route('/emails', methods=['GET'])
def get_cold_emails():
    emails = [{
        "id": 1,
        "status": EmailStatus.SENT.value,
        "contact_name": "Lang Chain",
        "contact_email": "langchain@mail.com",   
        "message": DUMMY_EMAIL,
        "created_at":  datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    },
    {
        "id": 2,
        "status": EmailStatus.SENT.value,
        "contact_name": "Dina Mitrov",
        "contact_email": "dinamitrov@mail.com",  
        "message": DUMMY_EMAIL,
        "created_at":  datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    }]

    return create_response(CustomStatusCode.SUCCESS.value, SUCCESS_MESSAGE, {"emails": emails}), 200

@routes_blueprint.route('/emails/<int:id>', methods=['GET'])
@ValidateParameters(url_validation_error_handler)
def get_email(id:int = Route()):
    email = get_record_by_field(Email, 'id', id).serialize()
    return create_response(CustomStatusCode.SUCCESS.value, SUCCESS_MESSAGE, email), 200