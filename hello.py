from flask import Flask, redirect, url_for,render_template,request
import time
import os
import operations
import database
import psycopg2
app = Flask(__name__)


@app.route('/login')
def login():
    return render_template('/index.html')

@app.route('/')
def hello():   
    return "HOME"

@app.route('/forgotpassword')
def forgotpassword():
    print('1')
    return render_template('/forgotpassword.html',output = "hide")


@app.route('/loginCred', methods = ['POST'])
def loginCred():
    user=request.form['userName']
    password=request.form['Password']
    if(operations.operationsUsernameCheck(user)):
       if(operations.operationsPasswordCheck(user,password)):
           print(user,password)
           return render_template('/newpage.html', output ='Login SuccessFul') 
       else:
             return render_template('/index.html', output ='Wrong Passoword')

    else:      
        return render_template('/index.html',output ='User Not Found. register User')


@app.route('/usercheck', methods = ['POST'])
def newpassowrd():
     user=request.form['userName']
     if(operations.operations(dict,user)):
       return render_template('forgotpassword.html', output = "show")
     else:
       return render_template('forgotpassword.html', output = "hide")


if __name__ == '__main__':
   port = int(os.getenv('PORT', 5000))
   print("Starting app on port %d" % port)
   app.run(debug=True, port=port, host='0.0.0.0')



