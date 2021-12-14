from flask import Flask, render_template, request, redirect, jsonify
from models.user import User
from models.film import Employee
from db.DB import DB
import json

app = Flask(__name__)
db = DB()

@app.route('/', methods = ['POST', 'GET'])
def signin():
    if  request.method == 'POST':
        login = request.form['login']
        password = request.form['password']

        access = db.GetUser(login, password)

        if access == True:
            return redirect('/About')

    else:
        return render_template('signin.html')

@app.route('/signup', methods = ['POST', 'GET'])
def signup():
    if  request.method == "POST":
        name = request.form['name']
        login = request.form['login']
        password = request.form['password']

        user = User(name,login,password)

        db.WriteUser(user)
        return redirect('/')

    else:
        return render_template('signup.html')

@app.route('/About')
def about():
    return render_template('about.html')

@app.route('/main')
def mainh():
    data = db.GetAllEmployees()
    return render_template('main.html', data = data, len = len(data['Employee']))


@app.route("/ajax_add", methods=["POST", "GET"])
def ajax_add():
    if request.method == 'POST':
        txtname = request.form['txtname']
        txtdepartment = request.form['txtdepartment']
        txtphone = request.form['txtphone']
        print(txtname)
        if txtname == '':
            msg = 'Please Input name'
        elif txtdepartment == '':
            msg = 'Please Input Department'
        elif txtphone == '':
            msg = 'Please Input Phone'
        else:
            db.WriteEmployee(Employee(txtname,txtdepartment,txtphone))
            msg = 'New record created successfully'
    return jsonify(msg)


@app.route("/ajax_update", methods=["POST", "GET"])
def ajax_update():
    if request.method == 'POST':
        string = request.form['string']
        txtname = request.form['txtname']
        txtdepartment = request.form['txtdepartment']
        txtphone = request.form['txtphone']
        print(string)
        msg = 'Record successfully Updated'
    return jsonify(msg)


@app.route("/ajax_delete", methods=["POST", "GET"])
def ajax_delete():
    if request.method == 'POST':
        getid = request.form['string']
        print(getid)
        msg = 'Record deleted successfully'
    return jsonify(msg)

if __name__ == '__main__':
    app.run()