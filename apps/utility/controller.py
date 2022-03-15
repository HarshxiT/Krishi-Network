from flask import json
from werkzeug.exceptions import HTTPException
from run import app


@app.errorhandler(HTTPException)
def handle_Hexception(e):
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "error": e.description,
    })
    response.content_type = "application/json"
    return response,e.code

@app.errorhandler(Exception)
def handle_exception(e):
    
    response = json.dumps({
        "code": 400,
        "error": str(e),
    })
    return response,400