

'''
Purpose: This Flask application builds a quiz system that covers user registration and authentication, 
quiz topic selection, quiz taking, and reviewing quiz results. 

It utilizes Flask extensions such as Flask-Login for managing user sessions, 
Flask-WTF for form handling and validation, 
Flask-Bcrypt for password hashing, 
and Flask-SQLAlchemy for database operations.

'''

from flask import Flask, render_template, redirect, url_for, request, session, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user,LoginManager,login_required,logout_user,current_user, login_manager
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import InputRequired,Length,ValidationError, DataRequired, EqualTo, Email
from flask_bcrypt import Bcrypt
import email_validator
from quiz_qstns import *
import re
# Regular expression to find numeric values - not used in the provided snippet but could be for validation

numeric_pattern = re.compile(r'\d+') # TO extract some data from radio button options
# Secret key for session management and CSRF protection
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-kk'

# SQLite database configuration

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
bcyrpt = Bcrypt(app) # For encryoting password
# User model for SQLAlchemy

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(90), nullable=False)

# Registration form using Flask-WTF
class RegisterForm(FlaskForm):
    # Flask validators used to set constaints on form data.
    first_name = StringField(validators= [InputRequired(), Length(min=3 ,max =20)],render_kw ={"placeholder": "Firstname"})
    last_name =  StringField(validators= [InputRequired(), Length(min=3 ,max =20)],render_kw ={"placeholder": "LastName"})
    email = StringField(validators= [InputRequired(), Email()],render_kw ={"placeholder": "Email"})
    password = PasswordField(validators= [InputRequired(), Length(min=6 ,max =25)],render_kw ={"placeholder": "Password"})
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField("Register")
    
    # Custom validator to ensure email uniqueness
    def validate_email(self,email):
        existing_user_email = User.query.filter_by(email=email.data).first()
        if existing_user_email:
            raise ValidationError(
                "This email already exist. Please Choose different one")
       
        # Login form
class LoginF(FlaskForm):
    '''
    Login form fields
    '''
    password = PasswordField(validators= [InputRequired(), Length(min=6 ,max =25)],render_kw ={"placeholder": "Password"})
    email=  StringField(validators= [InputRequired(), Length (min=6 ,max =30)],render_kw ={"placeholder": "Email"})
    submit = SubmitField("Register")

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Route for the home page
@app.route('/')
def index():
    return render_template('base.html')

# Route for logging in
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user:
            return redirect(url_for('select_topic'))
        else:
            pass
    return render_template('base.html') # Direct to home page

# Route for user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcyrpt.generate_password_hash(form.password.data).decode('utf-8')
        new_user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            password=hashed_password
        )

        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        pass

    return render_template('register.html', form=form)

# Route for the dashboard, requires login
@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('dashboard.html')
# Route for logging out

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

# Route for selecting a quiz topic
@app.route('/select_topic', methods=['GET', 'POST'])
def select_topic():
    if request.method == 'POST':
        selected_topic = request.form.get('topic')
        session['selected_topic'] = selected_topic
        return redirect(url_for('show_questions'))
    return render_template('topic.html', topics=quiz_data.keys()) # Pass selected topic

# Route for displaying quiz questions
@app.route('/show_questions')
def show_questions():
    '''
    Function to display questions from the selected user topic
    '''
    selected_topic = session.get('selected_topic')
    if not selected_topic:
        return redirect(url_for('select_topic'))
    questions = quiz_data.get(selected_topic, [])
    return render_template('questions.html', topic=selected_topic, questions=questions)

# Route for submitting quiz answers and showing results
@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    '''
    Extract & compare user choices & selected answer to generate score, reciew answers & submit the Quiz
    '''
    selected_topic = session.get('selected_topic')
    if not selected_topic:
        return redirect(url_for('select_topic'))

    questions = quiz_data.get(selected_topic, [])
    user_answers = request.form.to_dict()

    results = []  # List to hold result data
    score = 0
    for idx, question in enumerate(questions):
        # Extracting the user's answer based on the question index
        user_answer = user_answers.get(f'question{idx + 1}')
        correct_answer = question['correct_answer']

        # Check if the user's answer is correct
        is_correct = user_answer == correct_answer
        if is_correct:
            score += 1

        results.append({
            'question': question['question'],
            'user_answer': user_answer or "No answer provided",  # Handle case where user didn't select an option
            'correct_answer': correct_answer,
            'is_correct': is_correct
        })

    # Instead of redirecting, render a template to review answers
    return render_template('review_answers.html', results=results, score=score, total_questions=len(questions))


@app.route('/score/<int:score>')
def score_page(score):
    return render_template('score.html', score=score)

@app.route('/check_db')
def check_db():
    '''
    Vanilla fucntion to check if the DB is functional.
    '''
    users = User.query.all()
    return render_template('check_db.html', users=users)

@app.route('/score', methods=['GET'])
@login_required
def show_score():
    # Assuming 'score' and 'total_questions' are stored in the session after quiz submission
    score = session.get('score', 0)
    total_questions = session.get('total_questions', 0)
    # Clear score information to start fresh on the next quiz attempt
    session.pop('score', None)
    session.pop('total_questions', None)
    return render_template('score.html', score=score, total_questions=total_questions)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8080) 
