from . import data_loader
from flask import Flask


def create_app(test_config=None):
    # create and configure the app instance ("app")
    #
    # __name__ is the name of the current Python module.
    # The app needs to know where it’s located to set up some paths,
    # and __name__ is a convenient way to tell it that.
    #
    # instance_relative_config=True tells the app that configuration
    # files are relative to the instance folder. The instance folder
    # is located outside the flaskr package and can hold local data that
    # shouldn’t be committed to version control, such as configuration
    # secrets and the database file.
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        print('foo')
        return 'Hello, World!'


    # Blueprint - API
    from . import api
    app.register_blueprint(api.bp)

    return app
