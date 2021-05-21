from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Survey:
    @staticmethod
    def validate_survey(survey):
        results = connectToMySQL('dojo_survey_schema')
        is_valid = True 
        if len(survey['name']) < 1:
            flash ("Name must be at least 1 character long*")
            is_valid = False
    
        if len(survey['comment']) < 1:
            flash ("Comments are required*")
            is_valid = False
            return is_valid