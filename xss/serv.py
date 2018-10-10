from flask import Flask,request,render_template, redirect, url_for, session, make_response

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
    users = [('timothy','1234'), ('akshay','abcd'), ('abinav','pass')]
    pair = (user,password)
    if pair in users:
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

@app.route('/search', methods=['GET'])
def search():
    print(request.args['searchString'])
    return render_template('search.html', term=request.args['searchString'])

@app.route('/post', methods=['POST'])
def post():
    print(request.form['postString'])
    posts.append(request.form['postString'])
    return render_template('home.html', posts=posts)

'''
    if 'userid' in session and session['userid']!='admin':
        return render_template('feedback.html',name=session['user'],question=question[session['type']],type=session['type'][0].upper()+session['type'][1:])
    elif 'userid' in session and session['userid']=='admin':
        return showResults()
    else:
        return render_template('index.html',myText='Please enter the following details to continue',submitLink="/login")

@app.route("/login",methods=["POST"])
def login():
    uType=request.form['type']
    result=[]
    with dbHelper() as db:
        result=db.getId(request.form['username'],request.form['type'],request.form['password'])
    if(len(result)>0):
        userid=result[0][0]
        already=False
        with dbHelper() as db:
            already=db.checkFeedback(userid)
        if(already):
            return render_template('index.html',myText='You have already given Feedback. Please login at a different time.',submitLink='/login')
        session['userid']=str(userid)
        session['user']=request.form['username']
        return render_template('feedback.html',name=request.form['username'],question=question[request.form['type']],type=uType[0].upper()+uType[1:])
    else:
        return render_template('index.html',myText='The details you provided did not match any records. Please try again.',submitLink='/login')

@app.route("/submit",methods=["POST"])
def submit():
    if 'userid' not in session:
        return render_template('index.html',myText='Please enter the following details to continue')
    with dbHelper() as db:
        db.insertFeedback(session['userid'],request.form)
    return render_template('signout.html')

@app.route("/logout")
def logout():
    if 'userid' not in session:
        return redirect('/')
    username=session['userid']
    session.pop('userid', None)
    if username=='admin':
        return redirect('/admin')
    else:
        return redirect('/')
'''

if __name__ == '__main__':
    app.secret_key='abcdefghijklmnopqrstuvwxyz'
    app.run("localhost", debug=True)
