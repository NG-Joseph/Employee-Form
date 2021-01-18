from main import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date

class Employee(db.Model): #notice that the class extends db.Model
    __tablename__= 'employee_db1'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), unique=False, nullable=False)
    lastname = db.Column(db.String(20), unique=True, nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False, default=date.today())
    mode_of_employment = db.Column(db.String(50), unique=False, nullable=False)
    nationality = db.Column(db.String(50), unique=False, nullable=False)
    job_title = db.Column(db.String(100), unique=False, nullable=False)

# represent the object when it is queried for
    def __repr__(self):
        return '<Register {}>'.format(self.id)


