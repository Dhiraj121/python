from flask import Flask

app=Flask(__name__)

@app.route('/hello')
def say_hello():
    return "Hello"
	
@app.route("/hello")
def say_hello():
    return "welcome"
	
if __name__=="__main__":
    app.run(host='localhost',prot=2004,debug=True)
