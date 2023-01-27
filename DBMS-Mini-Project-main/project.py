from flask import Flask,redirect,render_template,url_for,request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Rushi.11'
app.config['MYSQL_DB'] = 'flask'
 
mysql = MySQL(app)

@app.route('/')
def root():
    return render_template('root.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/abc',methods=['POST', 'GET'])
def abc():
    output = request.form.to_dict()
    print(output)
    name = output["name"]
    return render_template('categories.html', name = name)

@app.route('/mobiles')
def mobiles():
    return render_template('mobiles.html')



@app.route('/sports')
def sports():
    return render_template('sports.html')

@app.route('/furniture')
def furniture():
    return render_template('furniture.html')

@app.route('/electronics')
def electronics():
    return render_template('electronics.html')
if __name__=="__main__":
        app.run(debug=True,port=7777)