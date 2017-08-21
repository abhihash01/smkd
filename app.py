from flask import Flask, render_template, request, session, redirect, make_response
import datetime

app = Flask(__name__)
@app.route('/home')
@app.route('/')
def main():
		return render_template('home.html')

#levels start 
@app.route('/level1')
def level1():
	return render_template("level11.html")

#LEVEL 1 Check
@app.route('/level1/hello')
def truelevel2():
	return redirect('/level2')

@app.route('/level2')
def level2():
	return render_template("level1.html")

@app.route('/level2/diamond')
def lvl3():
	return redirect('/level3')

@app.route('/level3')
def level3():
        return render_template("level3.html")

@app.route('/level3/<path>')
def validateLevel3(path = ""):
	if path == 'mist':
		return redirect('/sweethome')

@app.route('/sweethome')
def level4():
	return redirect("level4.html")

@app.route('/sweethome/index')
def index():
	return redirect('/pagenotfound')

@app.route('/pagenotfound')
def pagenotfound():
	return render_template("level5.html")

if __name__=='__main__':
   app.run(debug=True) 

