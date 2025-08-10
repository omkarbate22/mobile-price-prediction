from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import numpy as np
import uvicorn
import config  # Import config

# Load model
with open(config.MODEL_PATH, "rb") as file:
    model = pickle.load(file)

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=config.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Input schema
class MobileSpecs(BaseModel):
    ram: float
    storage: float
    battery: float
    camera: float
    brand: str

@app.post("/predict")
def predict(data: MobileSpecs):
    brand_features = config.BRAND_MAPPING.get(data.brand, [0, 0, 0, 0])
    features = np.array([[data.ram, data.storage, data.battery, data.camera] + brand_features])
    price = model.predict(features)[0]
    return {"predicted_price": round(price, 2)}

if __name__ == "__main__":
    uvicorn.run(app, host=config.HOST, port=config.PORT)
