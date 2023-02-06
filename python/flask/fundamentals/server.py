from flask import Flask , render_template

app= Flask(__name__)

@app.route('/')

def hello():
 
 return "hello from server.py"   

@app.route('/hello/<name>/<times>')

def say_hi(name,times):
    # return f"hello {name}😊👌✌" * int(times)
    return render_template("index.html" , user = name , times=times)
    

if __name__ == '__main__' :
    app.run(debug=True, port=5001)
    
