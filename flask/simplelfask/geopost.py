#integrate the HTML file with Flasek
#render_template hlep to redirect to the html file (jinja 2 )
from flask import Flask,render_template ,request
"""
It creates an instances of the flask class,
which will be your WGSI application
"""
#WSGI application
app=Flask(__name__)

@app.route("/") # / homepage
def  welcome():
    return "<html><h2>welcome to the flask</h2></html>"


@app.route("/index",methods=['GET']) # / homepage
def  index():
    return render_template('index.html')
@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f"name {name}"
    return render_template('form.html')

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f"name {name}"
    return render_template('form.html')

if __name__=="__main__":
    app.run(debug=True,port=8000)
    #debug =True for the work relaod automaticaly with out restarting the server
    
