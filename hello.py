from flask import Flask, redirect, url_for,render_template,request
import time
import os
app = Flask(__name__)



@app.route('/admin')
def hello_admin():
   return 'Hello Admin'
     

@app.route('/')
def hello():   
    return "HOME"

if __name__ == '__main__':
   port = int(os.getenv('PORT', 5000))
   print("Starting app on port %d" % port)
   app.run(debug=True, port=port, host='0.0.0.0')



