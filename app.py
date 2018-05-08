from flask import Flask, request, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import Form

app = Flask(__name__)
Bootstrap(app)



@app.route("/", methods=['GET'])
def index():
	return render_template('index.html')




if __name__ == "__main__":
	app.run(debug=True)