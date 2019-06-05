from flask import Flask, redirect, url_for,render_template,request
import time
import os
import operations
app = Flask(__name__)



dict = {'AA001': 'AA001', 'AA002': 'AA002'}
@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route('/login')
def login():
    return render_template('/index.html')

@app.route('/forgotpassword')
def forgotpassword():
    print('1')
    return render_template('/forgotpassword.html',output = "hide")

@app.route('/loginCred', methods = ['POST'])
def loginCred():
    user=request.form['userName']
    password=request.form['Password']
    
    if user in dict:
        if (dict.get(user)==password):
           
           return render_template('/newpage.html', output ='Login SuccessFul')
         
        else:
             return render_template('/index.html', output ='Wrong Passoword')

    else:      
        return render_template('/index.html',output ='User Not Found. register User')

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))

@app.route('/usercheck', methods = ['POST'])
def newpassowrd():
     user=request.form['userName']
     print('userss')
     if(operations.operations(dict,user)):
       print('usersss34')
       return render_template('forgotpassword.html', output = "show")
     else:
       return render_template('forgotpassword.html', output = "hide")
     

@app.route('/')
def hello():   
    return operations.forgotpassword

if __name__ == '__main__':
   port = int(os.getenv('PORT', 5000))
   print("Starting app on port %d" % port)
   app.run(debug=True, port=port, host='0.0.0.0')



