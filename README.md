# Prerequisites


```bash
python3 -m venv venv
source venv/bin/activate  
pip install -r requirements.txt
```

# Installing

Clone the repository:
```bash
git clone https://github.com/yourusername/yourprojectname.git
```

Navigate to the project directory:
```
bash
cd yourprojectname
```

Install the requirements:
```
bash
pip install -r requirements.txt
```

Run the Flask application:
```
bash
export FLASK_APP=app.py  # On Windows use `set FLASK_APP=app.py`
export FLASK_ENV=development  # On Windows use `set FLASK_ENV=development`
flask run
```

Visit http://127.0.0.1:8080/ in your web browser to view the application.
