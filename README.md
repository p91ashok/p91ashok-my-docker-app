# DevOps Demo Dashboard

A Flask web application for practicing GitHub, Jenkins, Docker and AWS CI/CD.

## Run locally

```bash
python -m venv .venv
```

Windows:
```powershell
.venv\Scripts\Activate.ps1
```

Git Bash:
```bash
source .venv/Scripts/activate
```

Linux/macOS:
```bash
source .venv/bin/activate
```

Install:
```bash
pip install -r requirements.txt
```

Run:
```bash
python app.py
```

Open:
http://localhost:5000

Health:
http://localhost:5000/health

## Run with Docker

```bash
docker build -t devops-demo .
docker run --rm -p 5000:5000 devops-demo
```

Open:
http://localhost:5000
