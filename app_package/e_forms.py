from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField,SelectField,DateField
from wtforms.validators import DataRequired,Email,NumberRange,Length

class EnquiryForm(FlaskForm):
    name=StringField("Name", validators=[DataRequired()])
    mobno=StringField("Mobile no", validators=[DataRequired(message="Enter Your Phone Number"),Length(min=10, max=10,message="Please enter a valid mobile number")])
    email = StringField('Email', [Email(message='Not a valid email address.'),DataRequired()])
    yearofpass=IntegerField("Year of Passout", validators=[DataRequired(message="Enter Your Year of Passout"),NumberRange(min=1990,max=2020,message="Please enter a valid year")])
    highqual=StringField("Highest Qualification", validators=[DataRequired()])
    location=StringField("Location", validators=[DataRequired()])
    prefercourse=SelectField("Prefered Course", choices=[('java','java'),('python','python'),('c++','c++'),('angular','angular'),('c','c')])
    source=SelectField("Source", choices=[('automatic','automatic'),('manual','manual')])
    status=SelectField("Enquiry Status", choices=[('done','done'),('interested','interested'),('pass','pass'),('fail','fail'),('join','join')])
    submit=SubmitField("Submit")


class UpdateEnquiryForm(FlaskForm):
    name=StringField("Name")
    mobno=IntegerField("Mobile no")
    email = StringField("Email")
    yearofpass=StringField("Year of Passout")
    highqual=StringField("Highest Qualification ")
    location=StringField("Location ")
    prefercourse=SelectField("Prefered Course ",choices=[('java','java'),('python','python'),('c++','c++'),('angular','angular'),('c','c')])
    source=SelectField("Source", choices=[('automatic','automatic'),('manual','manual')])
    status=SelectField("Enquiry Status ", choices=[('done','done'),('interested','interested'),('pass','pass'),('fail','fail'),('join','join')])
    submit=SubmitField("Submit")
    
    
