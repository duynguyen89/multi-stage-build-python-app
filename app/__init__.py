from flask import Flask

def create_app(config_class=None):  # ← Add parameter
    app = Flask(__name__)
    
    # Configure from object if provided
    if config_class:
        app.config.from_object(config_class)
    
    # Late imports to avoid circular dependencies
    from .routes import bp
    app.register_blueprint(bp)
    
    return app