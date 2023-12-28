# Import the create_app function and main_bp blueprint from the TextCraftPro.app.routes module
from TextCraftPro.app.routes import create_app, main_bp

# Create the Flask application using the create_app function
app = create_app()

# Register the main_bp blueprint with the Flask application
app.register_blueprint(main_bp)