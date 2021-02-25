from flask import Flask

app = Flask(__name__)
home_page = '''

<!DOCTYPE html>
<html>
<body>

<h1>This is Home page</h1>
<h4>This is heading 4</h4>
<h5>This is heading 5</h5>


</body>
</html>

'''

@app.route('/')
def hello():
    return {'ok':1} 


@app.route('/index')
@app.route('/home')
def home():
    return home_page

app.run(debug=True)
