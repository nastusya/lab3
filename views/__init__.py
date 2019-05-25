from templates import *
from flask import *
from main import app
from models import *


@app.before_first_request
def create_tables():
    db.create_all(app=app)


@app.route('/users', methods=['GET'])
def index():
    visitors_list = VisitorModel.query.all()

    return render_template("index.html", visitors_list=visitors_list)


@app.route('/add-user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        new_visitor = VisitorModel(
            visitor_name=request.form['name'],
            visitor_surname=request.form['surname'],
            visitor_gender=request.form['gender'],
            visitor_email=request.form['email']
        )
        new_visitor.save_to_db()

        return redirect('/users')

    return render_template("add-visitor.html")


@app.route('/remove-visitor/<int:visitor_id>', methods=['GET'])
def remove_visitor(visitor_id):
    VisitorModel.query.filter_by(visitor_id=visitor_id).delete()
    db.session.commit()

    return redirect('/users')


@app.route('/edit-visitor/<int:visitor_id>', methods=['GET', 'POST'])
def edit_visitor(visitor_id):
    visitor_item = VisitorModel.query.filter_by(visitor_id=visitor_id).first()

    if request.method == 'POST':
        visitor_item.user_name = request.form['name']
        visitor_item.visitor_surname = request.form['surname']
        visitor_item.visitor_gender = request.form['gender']
        visitor_item.user_email = request.form['email']

        db.session.commit()

        return redirect('/visitors')

    return render_template("edit-visitor.html", user_id=visitor_id, first_name=visitor_item.visitor_name,
                           last_name=visitor_item.visitor_surname,gender=visitor_item.visitor_gender,
                           email=visitor_item.user_email)