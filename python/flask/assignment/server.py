from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello():
    return "hello world"

@app.route('/dojo')
def say_hey():
    return f"dojo"

@app.route('/say/<name>')
def say(name):
    return f"Hi {name}!"

@app.route('/repeat/<times>/<name>')
def repeat(name,times):
    return f"{name} <br>" *int(times) 
@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again."
    
if __name__ == "__main__" :
    app.run(debug=True, port=5000)
