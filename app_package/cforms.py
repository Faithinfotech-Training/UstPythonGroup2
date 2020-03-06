from flask_wtf import FlaskForm
from wtforms import StringField,FloatField,IntegerField,SubmitField,TextAreaField,SelectField
from wtforms.validators import DataRequired,NumberRange

class AddCourseForm(FlaskForm):
    name=StringField("Course name:",validators=[DataRequired(message="Please enter course name")])
    duration=IntegerField("Duration of course in days:",validators=[DataRequired(message="Please enter duration"),NumberRange(min=0,message="Enter valid duration")])
    fee=FloatField("Fee of course",validators=[DataRequired(message="Please enter valid fee"),NumberRange(min=1000,message="Enter valid fee with min 1000 rs")])
    status=SelectField("Status",choices=[('active','active'),('inactive','inactive')])
    description=TextAreaField("Description",validators=[DataRequired()])
    submit=SubmitField("ADD",validators=[DataRequired()])
    
class UpdateCourseForm(FlaskForm):
    duration=IntegerField("Duration of course in days:",validators=[DataRequired(message="Please enter duration"),NumberRange(min=0,message="Enter valid duration")])
    fee=FloatField("Fee of course",validators=[DataRequired(message="Please enter valid fee"),NumberRange(min=1000,message="Enter valid fee  with min 1000 rs")])
    status=SelectField("Status",choices=[('active','active'),('inactive','inactive')])
    submit=SubmitField("UPDATE",validators=[DataRequired()])
