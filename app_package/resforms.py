from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,IntegerField,RadioField,FloatField,SubmitField
from wtforms.validators import DataRequired,EqualTo,ValidationError,NumberRange,Length

class AddResourceForm(FlaskForm):
    resourcename=StringField("Resource Name",validators=[DataRequired()])
    seatcapacity=IntegerField("Seat Capacity",validators=[DataRequired(message="Please enter a valid seat capacity"),NumberRange(min=0)])
    rent=FloatField("Rent per days",validators=[DataRequired(message="Please enter a valid rent "),NumberRange(min=0)])
    usetype=SelectField("Type of use", choices = [('training','training'),('seminar','seminar'),('gd','gd')])
    submit=SubmitField("Confirm")

class UpdateResourceForm(FlaskForm):
    rent=FloatField("Rent per days",validators=[DataRequired(message="Please enter a valid rent ")])
    status=SelectField("Resource Status",choices=[('occoupied','occoupied'),('available','available'),('booked','booked')])    
    usetype=SelectField("Type of use", choices = [('training','training'),('seminar','seminar'),('gd','gd')])
    submit=SubmitField("Confirm")