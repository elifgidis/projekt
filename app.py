from flask import Flask, render_template, redirect, url_for, request, session, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user,LoginManager,login_required,logout_user,current_user, login_manager
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import InputRequired,Length,ValidationError, DataRequired, EqualTo, Email
from flask_bcrypt import Bcrypt
import email_validator

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-kk'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
bcyrpt = Bcrypt(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) # 
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(90), nullable=False)

class RegisterForm(FlaskForm):
    first_name = StringField(validators= [InputRequired(), Length(min=3 ,max =20)],render_kw ={"placeholder": "Firstname"})
    last_name =  StringField(validators= [InputRequired(), Length(min=3 ,max =20)],render_kw ={"placeholder": "LastName"})
    email = StringField(validators= [InputRequired(), Email()],render_kw ={"placeholder": "Email"})
    password = PasswordField(validators= [InputRequired(), Length(min=6 ,max =25)],render_kw ={"placeholder": "Password"})
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField("Register")

    def validate_email(self,email):
        existing_user_email = User.query.filter_by(email=email.data).first()
        if existing_user_email:
            raise ValidationError(
                "This email already exist. Please Choose different one")
        
class LoginF(FlaskForm):
    password = PasswordField(validators= [InputRequired(), Length(min=6 ,max =25)],render_kw ={"placeholder": "Password"})
    email=  StringField(validators= [InputRequired(), Length (min=6 ,max =30)],render_kw ={"placeholder": "Email"})
    submit = SubmitField("Register")

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user:
            print('Form confirmation')
            return redirect(url_for('select_topic'))
        else:
            print('Invalid username or password')
            flash('Invalid username or password')
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    print('form first_name:', form.first_name.data)
    print('form last_name:', form.last_name.data)
    print('form email:', form.email.data)
    print('form password:', form.password.data)
    print('form check password:', form.confirm_password.data)
    if form.validate_on_submit():
        hashed_password = bcyrpt.generate_password_hash(form.password.data).decode('utf-8')
        print('hashed_password :',hashed_password)
        # new_user = User(email = form.username.data, password = hashed_password)
        new_user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            password=hashed_password
        )
        print('new user', new_user)
        print('Trying to commit to DB')
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login'))
    else:
        print('Trying to commit to DB, form validation failed')

    return render_template('register.html', form=form)

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

topics_questions = {
    'History': [
        {'text': 'Which civilisation is the oldest in the world?', 'options': ['Egyptian', 'Mesopotamian', 'Indus', 'Chinese']},
        {'text': 'Which word is an antonym for "Ancient"?', 'options': ['Old', 'Modern', 'Rare', 'Typical']},
        {'text': 'What is the past tense of "Run"?', 'options': ['Ran', 'Running', 'Runed', 'Runs']}],
    'Politics': [
        {'text': 'What is the synonym of "Beautiful"?', 'options': ['Pretty', 'Ugly', 'Weak', 'Fast']},
        {'text': 'Which word is an antonym for "Ancient"?', 'options': ['Old', 'Modern', 'Rare', 'Typical']},
        {'text': 'What is the past tense of "Run"?', 'options': ['Ran', 'Running', 'Runed', 'Runs']}
    ],
    'English': [
        {'text': 'What is the synonym of "Beautiful"?', 'options': ['Pretty', 'Ugly', 'Weak', 'Fast']},
        {'text': 'Which word is an antonym for "Ancient"?', 'options': ['Old', 'Modern', 'Rare', 'Typical']},
        {'text': 'What is the past tense of "Run"?', 'options': ['Ran', 'Running', 'Runed', 'Runs']}
    ],
   
}

quiz_data = {
        'History': 
        [
        {"question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "correct_answer": "Paris"},
        {"question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "correct_answer": "Paris"},
        ],
        'Politics': 
        [
        {"question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Venus", "Jupiter", "Saturn"],
        "correct_answer": "Mars"},
        {"question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "correct_answer": "Paris"},
        ]
    # Add more questions as needed
}

@app.route('/select_topic', methods=['GET', 'POST'])
def select_topic():
    if request.method == 'POST':
        selected_topic = request.form.get('topic')
        session['selected_topic'] = selected_topic
        return redirect(url_for('show_questions'))
    return render_template('topic.html', topics=quiz_data.keys())
    # return render_template('topic.html', topics=topics_questions.keys())

@app.route('/submit_topic', methods=['POST'])
def submit_topic():
    selected_topic = request.form.get('topic')
    session['selected_topic'] = selected_topic
    return redirect(url_for('show_questions'))

@app.route('/show_questions')
def show_questions():
    selected_topic = session.get('selected_topic')
    if not selected_topic:
        return redirect(url_for('select_topic'))
    # questions = topics_questions.get(selected_topic, [])
    questions = quiz_data.get(selected_topic, [])
    print('questions show_qstns:', questions)
    return render_template('questions.html', topic=selected_topic, questions=questions)

@app.route('/submit_quiz_', methods=['POST'])
@login_required
def submit_quiz_():
    print('submit_quiz ', submit_quiz)
    selected_topic = session.get('selected_topic')
    print('selected_topic ', selected_topic)
    if not selected_topic:
        return redirect(url_for('select_topic'))

    # questions = topics_questions.get(selected_topic, [])
    questions = quiz_data.get(selected_topic, [])
    print('questions ', questions)
    submitted_answers = {q: request.form.get(f'question{idx}') for idx, q in enumerate(questions, start=1)}
    print('Quiz submitted successfully!')
    flash('Quiz submitted successfully!')
    return redirect(url_for('index'))


@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    selected_topic = session.get('selected_topic')
    print('selected_topic ', selected_topic)
    if not selected_topic:
        return redirect(url_for('select_topic'))
    questions = quiz_data.get(selected_topic, [])
    print('questions ', questions)
    # submitted_answers = {q: request.form.get(f'question{idx}') for idx, q in enumerate(questions, start=1)}
    user_answers = request.form.to_dict()
    indexes = []
    for k in user_answers.keys():
        idxAnswer = int(numeric_pattern.search(k).group())
        indexes.append(idxAnswer)
    crctAnswers=[]
    for idx, qstn in enumerate(questions):
        ans = qstn['correct_answer']
        crctAnswers.append(ans)

    user_answer = []
    for k,v in user_answers.items():
        user_answer.append(v)

    print('user_answers:', user_answers)
    print('user_answer:', user_answer)
    print('crctAnswers:', crctAnswers)
    score = calculate_score(user_answer, crctAnswers)
    # Flash the score
    flash(f'Your score: {score} out of {len(quiz_data)}', 'success')
    return redirect(url_for('index'))

import re
numeric_pattern = re.compile(r'\d+')


def calculate_score(user_answer, crctAnswers):
    score = 0
    common = [i for i, j in zip(user_answer, crctAnswers) if i == j]
    score = len(common)
    return score

@app.route('/check_db')
def check_db():
    users = User.query.all()
    return render_template('check_db.html', users=users)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8080)