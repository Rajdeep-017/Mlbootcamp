from flask import Flask
"""
It creates an instances of the flask class,
which will be your WGSI application
"""
#WSGI application
app=Flask(__name__)

@app.route("/") # / homepage
def  welcome():
    return "welcome to flask course" 


@app.route("/index") # / homepage
def  index():
    return "welcome to flask course index page"  
if __name__=="__main__":
    app.run(debug=True,port=8080)
    #debug =True for the work relaod automaticaly with out restarting the server
    
