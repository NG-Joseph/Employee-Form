from flask import Flask, render_template, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/employee1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


import models




db = SQLAlchemy(app)







@app.route("/")
def signup():
    return render_template('newemployee.html', title="SIGN UP", information="Enter The Employee Details Below")

@app.route("/process-signup/", methods=['POST'])
def process_signup():
    id = request.form['id']
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    date_of_birth = request.form['date_of_birth']
    nationality = request.form['nationality']
    job_title = request.form['job_title']
    mode_of_employment = request.form['mode_of_employment']

    try:
        employee = models.Employee(id=id, firstname=firstname, lastname=lastname, date_of_birth=date_of_birth, nationality=nationality, job_title=job_title, mode_of_employment=mode_of_employment)
        db.session.add(employee)
        db.session.commit()

    except Exception as e:
        information = 'Login Unsuccessful. {}.'.format(e.__cause__)
        return render_template('newemployee.html', title="Welcome", information=information)

    information = 'Employee, {} {} successfully added.'.format(firstname, lastname)
    return render_template('newemployee.html', title="New Staff", information=information)











if __name__ == "__main__":
    app.run()

