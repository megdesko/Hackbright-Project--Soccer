from flask.ext.wtf import Form, validators
from flask.ext.wtf import FloatField, TextField, PasswordField, IntegerField, DateField, BooleanField, SelectField, RadioField, SelectMultipleField
import model

class LoginForm(Form):
	email = TextField('Email',
		              [validators.Email(message= (u'Invalid email address'))])
	password = PasswordField('Password', [validators.Required(), 
							 validators.length(min=6, max=25)])
										  					
class RegisterForm(Form):
	firstname = TextField('First Name', [validators.Required()], 
						  description=u'First Name')
	lastname = TextField('Last Name',[validators.Required()], 
						 description=u'Last Name')
	email = TextField('Email',[validators.Email(message= (u'Invalid email address'))], 
					  description=u'Email')
	password = PasswordField('Password', [validators.Required(), 
							 validators.length(min=6, max=25)], description=u'Password')
	address= TextField('Address',[validators.Required()], 
					   description=u'Address')
	city= TextField('City',[validators.Required()], description=u'City')
	state = TextField('State', [validators.Required(), 
					  validators.length(max=2)], description=u'State')
	zipcode = TextField('Zipcode', [validators.Required()], description=u'Zipcode')
	country = TextField('Country',[validators.Required()], description=u'Country')
	dob = DateField('DOB', [validators.Required(message= (u'Enter birthdate: mm/dd/yyyy'))], 
					format= '%m/%d/%Y', description=u'Date of Birth (mm/dd/yyyy)')
	gender = RadioField('Gender', [validators.Required()], 
						choices=[('male', 'M'),('female','F')], description=u'Gender')
	fitness = SelectField('Fitness Level', [validators.Required()], 
						  choices=[ ('1', 'low'), ('2', 'medium'), ('3', 'high')], 
						  description=u'Fitness Level')
	# need to convert fitness value to int
	
	experience = SelectField('Years Played?', [validators.Required()], 
							 choices=[(str(i),i) for i in range(66)], 
							 description=u'Years Played?')
	# need to covert experience value to int
	
	willing_teamLeader = BooleanField('Team Leader?')

	positions = SelectMultipleField(u'Positions', 
									choices=[('offense', 'offense'), ('defense', 'defense'), 
											 ('midfield', 'midfield'), ('goalie','goalie')],
									description=u'Positions (Optional)')

	health = SelectMultipleField(u'Health Issues', [validators.Required()], 
									choices=[(str(i.id), i.issue) for i in model.session.query(model.HealthType).\
																	order_by(model.HealthType.id).all()],
									description=u'Health Issues')



class SeasonCycleForm(Form):
	leaguename = TextField('League Name', [validators.Required()],
							description=u'League Name')
	cyclename = TextField('Cycle Name', [validators.Required(), 
						   validators.length(min=6, max=25)],
						   description=u'Season Cycle Description')
	num_of_teams = IntegerField('Number Of Teams', [validators.Required()])
	home_region = TextField('League Name', [validators.Required()])
	fee_resident = FloatField('Resident Fee', [validators.Required()])
	fee_nonresident = FloatField('Resident Fee', [validators.Optional()]) 
	reg_start = DateField('Registration Starts', [validators.Required(message=(u'start date: mm/dd/yyyy'))], 
						   format= '%m/%d/%Y', description=u'Registration Starts (mm/dd/yyyy)')
	reg_end = DateField('Registration Ends', [validators.Required(message= (u'end date: mm/dd/yyyy'))], 
						 format= '%m/%d/%Y', description=u'Registration Ends (mm/dd/yyyy)')

########## End Forms

def length(min=-1, max=-1):
    message = 'Must be between %d and %d characters long.' % (min, max)

    def _length(form, field):
        l = field.data and len(field.data) or 0
        if l < min or max != -1 and l > max:
            raise ValidationError(message)

    return _length