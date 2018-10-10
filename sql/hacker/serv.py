from flask import Flask,request,render_template, redirect, url_for, session, make_response

app=Flask(__name__,static_url_path="")

@app.route('/', methods=['GET'])
def func():
    print('Received GET Request')
    print('Received Cookie:', request.args)
    return ('', 204)

if __name__ == '__main__':
    app.secret_key='abcdefghijklmnopqrstuvwxyz'
    app.run("localhost", port=1234, debug=False)
