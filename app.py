from flask import Flask, render_template, request, jsonify
import db
import os
import sqlite3

# Application Flask for Quiz App

# Initialize the Flask application
app = Flask(__name__)

# Configure the application
app.config.from_mapping(
    SECRET_KEY='secret_key_just_for_dev_environment',
    DATABASE=os.path.join(app.instance_path, 'todos.sqlite')
)

# ... (rest of your setup code)

@app.route('/lists/')
def lists():
    db_con = db.get_db_con()
    # ... (existing code to fetch lists)
    
    if request.args.get('json') is not None:
        return jsonify(lists)
    else:
        return render_template('lists.html', lists=lists)

@app.route('/lists/<int:id>')
def list(id):
    db_con = db.get_db_con()
    # ... (existing code to fetch specific list details)

    if request.args.get('json') is not None:
        list['todos'] = [dict(todo) for todo in list['todos']]
        return jsonify(list)
    else:
        return render_template('list.html', list=list)

# ... (rest of your Flask app code)

if __name__ == "__main__":
    app.run(debug=True)