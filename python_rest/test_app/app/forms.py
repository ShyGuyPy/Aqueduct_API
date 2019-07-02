from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField
from wtforms.validators import ValidationError,DataRequired,Email, EqualTo
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me =BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class DataForm(FlaskForm):
    start_date = DateField('enter search start date', validators=[DataRequired()])
    end_date = DateField('enter search end date', validators=[DataRequired()])

    res = BooleanField('res') #, validators=[DataRequired()])
    solids = BooleanField('solids')
    NTU = BooleanField('NTU')
    org_ml = BooleanField('org_ml')
    MPN_100ml = BooleanField('MPN_100ml')
    MPN_100ml_1 = BooleanField('MPN_100ml_1')
    LosR = BooleanField('LosR')

    Silica = BooleanField('Silica')
    Ca = BooleanField('Ca')
    Mg = BooleanField('Mg')
    Ca_Mg = BooleanField('Ca_Mg')
    NO3 = BooleanField('NO3')
    NO3_USGS = BooleanField('NO3_USGS')

    Cl2 = BooleanField('Cl2')
    Na = BooleanField('Na')
    SO4 = BooleanField('SO4')
    K = BooleanField('K')
    pH = BooleanField('pH')
    Alk = BooleanField('Alk')

    Hard = BooleanField('Hard')
    Nhard = BooleanField('Nhard')
    C_USGSTemp = BooleanField('C_USGSTemp')
    F_USGS = BooleanField('F_USGS')
    Temp = BooleanField('Temp')
    MD_Precip_inch_mon = BooleanField('MD_Precip_inch_mon')
    MD_Temp_F = BooleanField('MD_Temp_F')

    submit = SubmitField('get data')

