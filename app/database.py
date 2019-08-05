from flask import Flask
from flaskext.mysql import MySQL
 
mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'beproject'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Beproject'
app.config['MYSQL_DATABASE_DB'] = 'dock_engine'
app.config['MYSQL_DATABASE_HOST'] = 'dockengine.cxd6jyo8ikqn.us-east-1.rds.amazonaws.com'
mysql.init_app(app)
 
@app.route("/")
def hello():
    return "Welcome to Python Flask App!"
 
if __name__ == "__main__":
    app.run()
