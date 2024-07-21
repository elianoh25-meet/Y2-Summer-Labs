import random
from flask import Flask, render_template,request,redirect,url_for
app = Flask(__name__)


@app.route('/home', methods=['GET', 'POST'])
def home():
	if request.method == 'GET':
		return render_template("home.html")
	else:
		birth_month=request.form['month']
		return redirect(url_for('fortune',month=birth_month))

@app.route('/fortune/<month>')
def fortune(month):
	fortune10=["you will cry today",
	"You are doing an excellent job",
	"you will have a good day",
	"Do it !",
	"go to eat!",
	"You will find the answer you just have to wait",
	"Don't worry it will work",
	"It's not that you fail, you find ways in which it doesn't work",
	"Smile more and it will work",
	"Breathe, you will succeed in the important event you have"]
	if len(month)>9:
		return render_template("fortune.html",fortune=fortune10[9])
	else:
		luck_fortune =fortune10[len(month)]
		return render_template("fortune.html",fortune=luck_fortune)


if __name__ == '__main__':
    app.run(debug=True, port=3000)