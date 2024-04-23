from flask import Flask,request,render_template
app=Flask(__name__)
@app.route('/')
def home():
    return "This is home page Modified"

@app.route('/login',methods=["GET","POST"])
def login():
    if request.method =='POST':
        Uname=request.form['username']
        pswd=request.form['password']
        print(Uname)
    return render_template('file.html')    

if __name__ =='__main__':
    app.run(debug=True)





