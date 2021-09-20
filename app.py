
from flask import Flask,render_template,request,redirect
import Prediction


app = Flask(__name__)


@app.route('/')
def first_page():
    return render_template("index.html")

@app.route('/submit',methods = ['POST'])
def display():
    if(request.files):
        f = request.files['user_file']
        path = "./static/{}".format(f.filename)
        f.save(path)
        pred = Prediction.get_pred(path)
        if pred == 1:
            return render_template("positive.html",path  = path)
        return render_template("negative.html",path = path)
    else:
        redirect("home.html")

if __name__ == "__main__":
    app.run(debug=True,threaded=False)
