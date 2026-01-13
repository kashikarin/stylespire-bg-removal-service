# Background Removal Microservice

A lightweight Python microservice for automatic background removal from images, built as part of the **StyleSpire** project.

The service receives an image URL, removes its background using a deep learning model, isolates the main subject, and returns a clean PNG image with transparency.

---

## ✨ Features

- Background removal using a deep learning segmentation model (`u2netp`)
- Automatic detection and cropping of the main subject
- Stateless HTTP API
- Designed as an independent microservice
- Optimized for deployment on low-memory environments

---

## 🧠 Architecture Overview

This service is intentionally separated from the main application and runs as a **dedicated microservice**.

### High-level flow

1. The client sends an image URL to the API
2. The image is downloaded and validated
3. The background is removed using a preloaded ML segmentation model
4. The largest connected subject is detected and isolated
5. The final image is returned as a PNG with transparency

In other words, the request flows through the system as follows:  
**Client → API → Background Removal Model → Subject Selection → PNG Response**

The ML model is loaded **once at startup** and reused across requests to reduce latency and memory overhead.  
This design avoids repeated model initialization and keeps inference costs predictable, even in constrained environments.

---

## 🛠️ Tech Stack

- **Python** – Core language
- **FastAPI** – HTTP API framework
- **rembg** – Background removal library
- **u2netp** – Lightweight deep learning segmentation model
- **Pillow (PIL)** – Image loading and manipulation
- **NumPy** – Array-based image processing
- **SciPy** – Connected-component analysis for subject selection

---

## 🚀 API Usage

### Endpoint

```http
POST /remove-background
```

### Request Body

```json
{
  "image_url": "https://example.com/image.jpg"
}
```

### Response

- **Status:** `200 OK`
- **Content-Type:** `image/png`
- **Body:** PNG image with transparent background, cropped to the main subject

---

## ▶️ Running the Service Locally

### Prerequisites

- Python 3.9+
- `pip`
- Virtual environment (recommended)

### Setup

Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/background-removal-service.git
cd background-removal-service

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

### Run the server

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

The service will be available at:

`http://localhost:8000`

### Example Request

```bash
curl -X POST http://localhost:8000/remove-background \
  -H "Content-Type: application/json" \
  -d '{"image_url": "https://example.com/image.jpg"}' \
  --output result.png
```
---

## ❤️ Health Check

```bash
curl http://localhost:8000/health
```

### Expected Response

```json
{
  "status": "ok"
}
```

---

## ⚙️ Deployment Notes

- The service is designed to run with **a single worker**
- The ML model is loaded once at application startup
- Peak memory usage during inference is approximately **700–900MB**
- Successfully deployed on **Render** using a **1GB RAM** plan

This setup is intentionally optimized for **portfolio and demo usage**, prioritizing stability and clarity over high concurrency.

---

## 📄 License

MIT License