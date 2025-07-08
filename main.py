import os
from flask import Flask
from database.db import init_app

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY', 'dev'),
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    from database.db import init_app
    init_app(app)
    
    from routes.auth import bp as auth_bp
    from routes.blog import bp_blog as blog_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(blog_bp)
    
    return app

app = create_app()