from flask import Flask
app = Flask(__name__)

@app.route('/home')
def home():
  return "<html>Hi welcoming to the photo gallery containing three types of photos:food, pets,outer space.</html> <a href='/food1'>go to the first food photo</a>"
@app.route('/food1')
def food1 ():
  return "<html><img src=https://www.foodiesfeed.com/wp-content/uploads/2023/06/pouring-honey-on-pancakes.jpg </img><a href='/home'>home pg</a></html>"
if __name__ == '__main__':
    app.run(debug=True)