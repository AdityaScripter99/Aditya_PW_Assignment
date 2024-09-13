# Flask-WTF is a Flask extension that integrates the WTForms library, which provides useful features for creating and handling forms in a simple way for a Flask web application.
# WTForms is a Python library for working with forms and form fields. 
# It provides a flexible framework for creating forms, handling validation, and rendering forms in HTML. 
# In this article, let us understand how the Flask-WTF library handles web forms with a Signup form example. 
# Before handling forms, let us know the features, field types, and prerequisites needed to develop the Signup form application.

# Some of the key features of Flask-WTF include:

# Secure handling of forms: Flask-WTF automatically handles cross-site request forgery (CSRF) protection, which is a security measure to prevent unauthorized form submissions.

# Form rendering: Flask-WTF provides a simple way to render forms in HTML templates. It also supports various form field types, such as text fields, checkboxes, and select fields.

# Validation: Flask-WTF provides built-in validation for form fields, such as required fields, length constraints, and pattern matching. It also supports custom validation methods.

# File uploads: Flask-WTF can handle file uploads, which allows users to upload files through a form.

# Importing Libraries.. 
from flask import Flask, render_template, request 
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField 
from wtforms import DecimalField, RadioField, SelectField, TextAreaField, FileField 
from wtforms.validators import InputRequired 
from werkzeug.security import generate_password_hash 
  
app = Flask(__name__) 
app.config['SECRET_KEY'] = 'secretkey'
  
  
class MyForm(FlaskForm): 
    name = StringField('Name', validators=[InputRequired()]) 
    password = PasswordField('Password', validators=[InputRequired()]) 
    remember_me = BooleanField('Remember me') 
    salary = DecimalField('Salary', validators=[InputRequired()]) 
    gender = RadioField('Gender', choices=[ 
                        ('male', 'Male'), ('female', 'Female')]) 
    country = SelectField('Country', choices=[('IN', 'India'), ('US', 'United States'), 
                                              ('UK', 'United Kingdom')]) 
    message = TextAreaField('Message', validators=[InputRequired()]) 
    photo = FileField('Photo') 

    @app.route('/', methods=['GET', 'POST']) 
    def index(): 

        form = MyForm() 
        if form.validate_on_submit(): 
           name = form.name.data 
           password = form.password.data 
           remember_me = form.remember_me.data 
           salary = form.salary.data 
           gender = form.gender.data 
           country = form.country.data 
           message = form.message.data 
           photo = form.photo.data.filename 
           return f"Name: {name} < br > Password: {generate_password_hash(password)}
           <br > Remember me: {remember_me} < br > Salary: {salary} < br > Gender: {gender} 
           <br > Country: {country} < br > Message: {message} < br > Photo: {photo}"
    
        return render_template('flask_WTF.html', form=form) 
  
  
if __name__ == '__main__': 
    app.run() 