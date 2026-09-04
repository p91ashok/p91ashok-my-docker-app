from flask import Flask, render_template, jsonify
import socket
import platform
import os
from datetime import datetime, timezone

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "index.html",
        hostname=socket.gethostname(),
        platform=platform.system(),
        python_version=platform.python_version(),
        environment=os.getenv("ENVIRONMENT", "Development"),
        timestamp=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    )

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "DevOps Demo Dashboard",
        "hostname": socket.gethostname(),
        "timestamp": datetime.now(timezone.utc).isoformat()
    }), 200

@app.route("/api/info")
def info():
    return jsonify({
        "application": "DevOps Demo Dashboard",
        "version": "1.0.0",
        "environment": os.getenv("ENVIRONMENT", "Development"),
        "hostname": socket.gethostname(),
        "platform": platform.system(),
        "python_version": platform.python_version()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
