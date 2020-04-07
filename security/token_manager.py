from resources.app import app
from flask_jwt_extended import (
    JWTManager, jwt_optional, create_access_token,
    get_jwt_identity
)

jwt = JWTManager(app)
