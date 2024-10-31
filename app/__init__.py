from flask import Flask

def app():
    app = Flask(__name__)

    from .views import views
    app.register_blueprint(views)

    return app