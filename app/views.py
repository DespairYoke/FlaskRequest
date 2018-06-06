from flask import Flask,request
app = Flask(__name__)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login(request.form['username'],
                            request.form['password'])
        return "post"
    else:
        print(request.args.get("key"))
        return "get"

def do_the_login(username,password):
    print(username+"  "+password)
app.run(debug=True)