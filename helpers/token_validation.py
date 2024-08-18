from flask import request, jsonify
from functools import wraps
import jwt

import app_config as config

def validateJWT():
    token = None
    accountInformation = None

    try:
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return 400

        try:
            accountInformation = jwt.decode(token, key= config.TOKEN_SECRET, algorithms=["HS256"])
        except Exception as err:
            return 401

        return accountInformation

    except jwt.ExpiredSignatureError:
        return 401
    except:
        return 400 