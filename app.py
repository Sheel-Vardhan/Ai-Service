from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app)

    # Register routes
    from routes.describe import describe_bp
    from routes.recommend import recommend_bp
    from routes.analyze import analyze_bp   # 👈 NEW

    app.register_blueprint(describe_bp)
    app.register_blueprint(recommend_bp)
    app.register_blueprint(analyze_bp)      # 👈 NEW

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)