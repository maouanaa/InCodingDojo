from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def playon():
    return render_template("index.html",num=3,color="blue")
@app.route('/play/<int:num>')
def repeat(num):
     return render_template("index.html",num=num,color="blue")
@app.route('/play/<int:num>/<color>')
def coler(num,color):
     return render_template("index.html",num=num,color=color)

if __name__=="__main__":
    app.run(debug=True,port=5001)