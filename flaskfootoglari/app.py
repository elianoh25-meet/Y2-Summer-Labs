from flask import Flask
app = Flask(__name__)

@app.route('/home')
def home():
  return '''<html>Hi welcoming to the photo gallery 
  containing three types of photos:food, pets,outer space.</html> <a href='/food1'>go to the first food photo</a>
  <a href='/food2'>food2</a>
  <a href='/food3'>food3</a>
  <a href='/pet1'>pet1</a>
  <a href='/pet2'>pet2</a>
  <a href='/pet3'>pet3</a>
  <a href='/space1'>space1</a>
  <a href='/space2'>space2</a>
  <a href='/space3'>space3</a>'''


@app.route('/food1')
def food1 ():
  return '''<html><img src=https://www.foodiesfeed.com/wp-content/uploads/2023/06/pouring-honey-on-pancakes.jpg></html>
  <a href='/home'>home pj</a>
  <a href='/food2'>food2</a>
  <a href='/food3'>food3</a>
  <a href='/pet1'>pet1</a>
  <a href='/pet2'>pet2</a>
  <a href='/pet3'>pet3</a>
  <a href='/space1'>space1</a>
  <a href='/space2'>space2</a>
  <a href='/space3'>space3</a>'''

  

@app.route('/food2')
def food2 ():
  return '''<html><img src=https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRUDMhPpndCvGlsF_NF-j1olBZVn9Gg8QDerw&s</html>
  <a href='/home'>home pj</a>
  <a href='/food3'>food3</a>
  <a href='/pet1'>pet1</a>
  <a href='/pet2'>pet2</a>
  <a href='/pet3'>pet3</a>
  <a href='/space1'>space1</a>
  <a href='/space2'>space2</a>
  <a href='/space3'>space3</a>'''


@app.route('/food3')
def food3 ():
  return'''<html><img src=https://assets.cntraveller.in/photos
  /60f6d111a77bf98b83f5364c/1:1/w_1080,h_1080,c_limit/Ahmedabad%20Food%20Guide.jpg></html>
  <a href='/home'>home pj</a>
  <a href='/pet1'>pet1</a>
  <a href='/pet2'>pet2</a>
  <a href='/pet3'>pet3</a>
  <a href='/space1'>space1</a>
  <a href='/space2'>space2</a>
  <a href='/space3'>space3</a>'''

if __name__ == '__main__':
    app.run(debug=True)