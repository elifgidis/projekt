# Prerequisites


```bash
python3 -m venv venv      # On Windows use python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

# Installing

Clone the repository:
```
git clone https://github.com/elifgidis/projekt.git
```

Navigate to the project directory:
```
cd projekt
```

Run the Flask application:
```
export FLASK_APP=app.py   # On Windows use `set FLASK_APP=app.py`
export FLASK_ENV=development  # On Windows use `set FLASK_ENV=development`
python app.py
```

Visit http://127.0.0.1:8080/ in your web browser to view the application.
