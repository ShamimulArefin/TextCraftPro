from TextCraftPro.app.routes import create_app, main_bp

app = create_app()
app.register_blueprint(main_bp)