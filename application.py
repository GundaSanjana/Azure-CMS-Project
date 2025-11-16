"""
This script runs the FlaskWebProject application using a development server.
"""

from FlaskWebProject import app

if __name__ == '__main__':
    # Simple dev server: HTTP, port 5000, no reloader
    app.run(host='127.0.0.1', port=5000, debug=True, use_reloader=False)
