from flask import Flask
from views import views

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/was_soulja_boy_the_first_one_to")

if __name__ == "__main__":
    app.run(debug=True, port=8000)