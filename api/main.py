from fastapi import FastAPI  
import torch  
from models.onnx_export import load_onnx_model  

app = FastAPI()  
model = load_onnx_model("model.onnx")  

@app.post("/predict")  
def predict(image: bytes):  
    tensor = preprocess(image)  
    return {"prediction": model(tensor).argmax().item()}  