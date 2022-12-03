from app.routes import app
import os

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
