# Background Removal Service

FastAPI microservice for background removal using `rembg`.

## Run locally

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload