import os
from flask import Flask , url_for, render_template
from database.db import init_app, init_db
from routes.auth import bp

def create_app():
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(os.getcwd(), 'flaskr.sqlite'),
    )

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    init_app(app)
    
    
    return app

    
if __name__ == '__main__':
    app = create_app()
    app.register_blueprint(bp)
    app.run(debug=True)
