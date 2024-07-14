import os
from flask import Flask , url_for, render_template, redirect
from database.db import init_app, init_db
from routes.auth import bp
from routes.blog import bp_blog

def create_app():
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(os.getcwd(), 'flaskr.sqlite'),
    )

    # @app.route('/')
    # def hello():
    #     return redirect(url_for("auth.login"))

    init_app(app)
    
    app.register_blueprint(bp_blog)
    app.add_url_rule('/',endpoint='index')
    
    
    return app

    
if __name__ == '__main__':
    app = create_app()
    app.register_blueprint(bp)
    app.run(debug=True)
