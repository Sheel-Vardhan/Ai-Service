from flask import Flask, render_template
from flask_cors import CORS
import os

# ✅ NEW: preload model import
from services.model_loader import get_model


def create_app():
    app = Flask(__name__)
    CORS(app)

    # ✅ Preload sentence-transformer model at startup
    get_model()
    print("✅ SentenceTransformer model loaded successfully")

    # Register routes
    from routes.describe import describe_bp
    from routes.recommend import recommend_bp
    from routes.analyze import analyze_bp
    from routes.history import history_bp
    from routes.batch_process import batch_bp

    app.register_blueprint(describe_bp)
    app.register_blueprint(recommend_bp)
    app.register_blueprint(analyze_bp)
    app.register_blueprint(history_bp)
    app.register_blueprint(batch_bp)

    # HOME ROUTE
    @app.route("/")
    def home():
        return render_template("index.html")

    return app


app = create_app()

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=True
    )