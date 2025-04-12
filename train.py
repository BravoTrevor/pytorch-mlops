import pytorch_lightning as pl  
from models.lit_model import LitModel  
from hydra import initialize, compose  

# Load config  
with initialize(config_path="../configs"):  
    cfg = compose(config_name="mnist")  

# Train  
model = LitModel(cfg)  
trainer = pl.Trainer(accelerator="gpu", logger=pl.loggers.WandbLogger())  
trainer.fit(model)  