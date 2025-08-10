
# Model file path
MODEL_PATH = "model.pkl"

HOST = "127.0.0.1"
PORT = 8000

# Allowed frontend origins
ALLOWED_ORIGINS = ["*"]  # Or ["http://127.0.0.1:5500"]

# Brand encoding mapping
BRAND_MAPPING = {
    "OnePlus": [1, 0, 0, 0],
    "Realme": [0, 1, 0, 0],
    "Samsung": [0, 0, 1, 0],
    "Vivo": [0, 0, 0, 1]
}
