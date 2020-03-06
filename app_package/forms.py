from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, IntegerField
from wtforms import DateTimeField
#from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, ValidationError

class AddBatchForm(FlaskForm):
    
    b_name=StringField("Batch Name: ", validators=[DataRequired()])
    start_date=DateTimeField('start_date',validators=[DataRequired()])
    end_date=DateTimeField('end_date',validators=[DataRequired()])
    b_status=RadioField('batch status', choices = [('active','active'),('inactive','inactive')])
    c_id=StringField("Course id: ", validators=[DataRequired()])
    submit=SubmitField("Add Batch")

class ModifyBatchForm(FlaskForm):
    b_name=StringField("Batch Name: ")
    start_date=DateTimeField('start_date')
    end_date=DateTimeField('end_date')
    b_status=RadioField('Status: ', choices = [('active','active'),('inactive','inacive')])
    submit=SubmitField("Update")
