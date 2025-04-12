# PyTorch MLOps Starter 🚀🔥  

An end-to-end ML pipeline with PyTorch Lightning, experiment tracking, and cloud deployment. Perfect for deploying models as APIs or batch jobs.  

![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-EE4C2C.svg)  
![W&B](https://img.shields.io/badge/Weights_&_Biases-FFCC33.svg)  
![License](https://img.shields.io/badge/license-MIT-green)  

## Features  

### 1. **Reproducible Training**  
- PyTorch Lightning + Hydra for config management.  
- W&B logging (metrics, hyperparameters, artifacts).  

### 2. **Model Deployment**  
- Export to ONNX/TensorRT for production.  
- FastAPI REST API with Docker.  

### 3. **Cloud Scaling**  
- Preemptible GPU training on GCP/AWS.  
- Terraform scripts for infra-as-code.  

## Quick Start  
git clone https://github.com/your-username/pytorch-mlops.git  
cd pytorch-mlops  

# Install (Poetry recommended)  
pip install -r requirements.txt  

# Train (MNIST example)  
python train.py --config configs/mnist.yaml  

# Deploy API  
docker build -t ml-api . && docker run -p 8000:8000 ml-api  
