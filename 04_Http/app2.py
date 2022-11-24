from flask import Flask, redirect, url_for, request
app = Flask(__name__)


@app.route('/api',methods = ['POST', 'GET'])
def api():
   if request.method == 'POST':
       return "post response"
   else:
       return "get response"   

if __name__ == '__main__':
   app.run(debug = True)