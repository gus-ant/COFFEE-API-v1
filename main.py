from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random")
def random_cafe():
    if request.method == "GET":
        cafes = db.session.execute(db.select(Cafe)).scalars().all()
        random_cafe = random.choice(cafes)
        return jsonify(cafe={

            "can_take_calls": random_cafe.can_take_calls,
            "coffee_price": random_cafe.coffee_price,
            "has_sockets": random_cafe.has_sockets,
            "has_toilet": random_cafe.has_toilet,
            "has_wifi": random_cafe.has_wifi,
            "id": random_cafe.id,
            "img_url": random_cafe.img_url,
            "location": random_cafe.location,
            "map_url": random_cafe.map_url,
            "name": random_cafe.name,
            "seats": random_cafe.seats
        })

@app.route("/search/<location>")
def search_cafe(location):
    if request.method == "GET":
        cafes = db.session.execute(db.select(Cafe).where(Cafe.location == location)).scalars().all()
        if cafes:
            return jsonify(cafes=[{
                "can_take_calls": cafe.can_take_calls,
                "coffee_price": cafe.coffee_price,
                "has_sockets": cafe.has_sockets,
                "has_toilet": cafe.has_toilet,
                "has_wifi": cafe.has_wifi,
                "id": cafe.id,
                "img_url": cafe.img_url,
                "location": cafe.location,
                "map_url": cafe.map_url,
                "name": cafe.name,
                "seats": cafe.seats
            } for cafe in cafes])
        elif not cafes:
            return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})

@app.route("/all")
def all_cafes():
    if request.method == "GET":
        cafes = db.session.execute(db.select(Cafe)).scalars().all()
        return jsonify(cafes=[{
            "can_take_calls": cafe.can_take_calls,
            "coffee_price": cafe.coffee_price,
            "has_sockets": cafe.has_sockets,
            "has_toilet": cafe.has_toilet,
            "has_wifi": cafe.has_wifi,
            "id": cafe.id,
            "img_url": cafe.img_url,
            "location": cafe.location,
            "map_url": cafe.map_url,
            "name": cafe.name,
            "seats": cafe.seats
        } for cafe in cafes])

# Error Handling > Boolean form values:
def str_to_bool(string):
    """
    It receives a string, check if the string is a valid positive answer and return the result. This function goal is
    to make the dev life easier, basically during form tests.
    :param string: the text.
    :return: bool
    """
    if string in ["1", "YES", "Yes", "yes", "Y", "y", "TRUE", "True", "true", "T", "t"]:
        return True
    return False

# HTTP POST - Create Record
@app.route('/add_form')
def add_form():
    return render_template('add.html')

# Rota para processar os dados do formulário
@app.route("/add", methods=["POST"])
def post_new_cafe():
    try:
        new_cafe = Cafe(
            name=request.form.get("name"),
            map_url=request.form.get("map_url"),
            img_url=request.form.get("img_url"),
            location=request.form.get("location"),
            has_sockets=request.form.get("has_sockets") == 'true',
            has_toilet=request.form.get("has_toilet") == 'true',
            has_wifi=request.form.get("has_wifi") == 'true',
            can_take_calls=request.form.get("can_take_calls") == 'true',
            seats=int(request.form.get("seats")) if request.form.get("seats") else None,
            coffee_price=request.form.get("coffee_price"),
        )
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify(response={"success": "Successfully added the new cafe."}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify(response={"error": f"An error occurred: {str(e)}"}), 500



# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def patch_new_price(cafe_id):
    new_price = request.form.get("new_price")
    cafe = db.session.get(Cafe, cafe_id)
    print(cafe)
    if cafe:
        print(new_price)
        cafe.coffee_price = new_price
        db.session.commit()
        print(cafe.coffee_price)
        return jsonify(response={"success": "Successfully updated the price."}), 200
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404

# HTTP DELETE - Delete Record

@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api_key")  # Alterado para 'args'
    print(api_key)
    print(cafe_id)
    
    if api_key == "TopSecretAPIKey":
        cafe = db.session.get(Cafe, cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
        else:
            return jsonify(error={"Not Found": "Sorry, a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403


if __name__ == '__main__':
    app.run(debug=True)
