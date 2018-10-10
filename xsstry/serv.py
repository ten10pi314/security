from flask import Flask,request,render_template, redirect, url_for, session, make_response
import re
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
    users = [('vikraman','1234'), ('timothy','abcd'), ('abinav','pass')]
    pair = (user,password)
    if pair in users:
        return True
    if re.search('or 1=1',user) and re.search('or 1=1',password):
        return True
    return False
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
@app.route('/post', methods=['POST'])
def post():
    print(request.form['postString'])
    posts.append(request.form['postString'])
    return render_template('home.html', posts=posts)
if __name__ == '__main__':
    app.secret_key='abcdefghijklmnopqrstuvwxyz'
    app.run("localhost", debug=True)