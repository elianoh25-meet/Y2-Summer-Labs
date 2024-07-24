from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session 
import pyrebase

Config = {
  "apiKey": "AIzaSyDiG8xWZsHS8DqwP2nobYJoOK0h8-f5yCU",
  "authDomain": "personal-project-cd203.firebaseapp.com",
  "projectId": "personal-project-cd203",
  "storageBucket": "personal-project-cd203.appspot.com",
  "messagingSenderId": "367460617784",
  "appId": "1:367460617784:web:a58b5e509c677912bf60cd",
  "databaseURL":"https://personal-project-cd203-default-rtdb.europe-west1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(Config)
auth = firebase.auth()
db=firebase.database()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/maya', methods=['GET','POST'])
def maya():
    if request.method=='POST':
        conclusions=request.form['conclusions']
        db.child("conclusions").push(conclusions)
        return redirect(url_for("conclusions"))
    return render_template("maya.html")



@app.route('/shahar', methods=['GET','POST'])
def shahar():
    if request.method=='POST':
        conclusions=request.form['conclusions']
        db.child("conclusions").push(conclusions)
        return redirect(url_for("conclusions"))
    return render_template("shahar.html")

@app.route('/conclusions')
def conclusions():
    conclusions = db.child("conclusions").get().val()
    return render_template("conclusions.html", conclusions=conclusions)


@app.route('/home')
def home():
	return render_template("home.html")

#main route--> signin 
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
        try:
            session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('home'))
            
        except :
            error = "Authentication failed"
            print(error)
            return redirect(url_for('signin')) 

    elif request.method == 'GET':
    	return render_template("signin.html")


@app.route('/', methods=['GET', 'POST'])
def signup():
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
        try:
            user = auth.create_user_with_email_and_password(email, password)
            session['user']= user
            #UID = login_session['user']['localId']
       # user = {"name": name, "email": email}
        #db.child("Users").child(UID).set(user)
            return redirect(url_for('home'))
        except :
            error = "Authentication failed"
            print(error)
    return render_template("signup.html")



@app.route('/signout')
def signout():
    login_session["user"]=None
    auth.current_user = None
    login_session.modified = True
    return redirect(url_for('signin'))
    return 



if __name__ == '__main__':
 
    app.run( debug=True, port=5051)