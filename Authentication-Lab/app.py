from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app=Flask(__name__, template_folder='templates', static_folder='static')
 
firebaseConfig = {
  "apiKey": "AIzaSyCqeo9HCOoTQ9k5Fxh24DaTjg1U84ilCMk",
  "authDomain": "at-lab-8d96b.firebaseapp.com",
  "projectId": "at-lab-8d96b",
  "storageBucket": "at-lab-8d96b.appspot.com",
  "messagingSenderId": "599364319259",
  "appId": "1:599364319259:web:04582398952719ea2b60be",
  "databaseURL":""
}

firebase = pyrebase.initialize_app(firebaseConfig) 

auth = firebase.auth()


@app.route('/',methods=['GET','POST'])
def signup():
    if request.method == 'GET':
        return render_template("signup.html") 
    else: #if the method is post
        email = request.form['email']
        password = request.form['password']
        session['user'] = auth.create_user_with_email_and_password(email, password)
        session['quotes'] = []
        return (render_template("home.html"))



@app.route('/home', methods = ['GET','POST'])
def home():
    if request.method == 'POST':
        print(login_session['quotes'])
        quote = request.form['quotes']
        login_session['quotes'] = quote
        return redirect(url_for('thanks'))
    return render_template('home.html')







@app.route('/display')
def display():
    return (render_template("display.html"))






@app.route('/thanks')
def thanks():
    return (render_template("thanks.html"))






@app.route('/signin', methods=['GET','POST'])
def signin():
    if request.method=='GET':
        return render_template('signin.html')
    else:
        email = request.form['email']
        password = request.form['password']
        session['user'] = auth.create_user_with_email_and_password(email, password)
        session['quotes'] = []
        return (render_template("home.html"))



@app.route('/signout')
def signout():
    session["user"]=None
    auth.current_user = None
    return redirect(url_for('signin'))
    return 




if __name__ == '__main__':
    app.run(debug=True, port=3001)
