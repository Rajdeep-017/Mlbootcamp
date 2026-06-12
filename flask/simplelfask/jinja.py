#building url dynamically
#variable rule
#jinja 2 template engine
#jinja 2 template engine 
"""
{{ }} expression to print output in html
{%..%} conditional statement ,for loops
{#.....#} comments
"""

from flask import Flask,render_template ,request, redirect,url_for
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



@app.route('/submi',methods=['GET','POST'])
def submi():
    if request.method=='POST':
        name=request.form['name']
        return f"name {name}"
    return render_template('form.html')
#variable rule
@app.route('/success/<int:score>') #can only pass the int value
def success(score):
    # return "the marks got is" +  str(score)
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    return render_template('result.html',results=res)  #results=res additional variable which is acting like  a data source it has some value

@app.route('/successres/<int:score>') #can only pass the int value
def successres(score):
    # return "the marks got is" +  str(score)
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    
    exp={'score':score,"res":res}  #The value it has is in the form of key value pairs.

    return render_template('result1.html',results=exp) 

##if condition

@app.route('/successif/<int:score>') #can only pass the int value
def successif(score):
    
    
    return render_template('result.html',results=score)




#building url dynamically

@app.route('/fail/<int:score>') #can only pass the int value
def fail(score):
   
    return render_template('result.html',results=score)

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_sci=float(request.form['data_sci'])

        total_score=(science+maths+c+data_sci)/4
        print(total_score)
    else:
        return render_template('get_res.html')
    return redirect(url_for('successres', score=int(total_score)))  #redirect to thhe successres for the checking

if __name__=="__main__":
    app.run(debug=True,port=8000)