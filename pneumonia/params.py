import os


DATA_SOURCE = os.environ["DATA_SOURCE"]
FITTING_TARGET = os.environ["FITTING_TARGET"]
MODEL_TARGET = os.environ["MODEL_TARGET"]
DATA_RATIO = 1
DATA_BUCKET_NAME = os.environ["DATA_BUCKET_NAME"]
DATA_BUCKET_URI = os.environ["DATA_BUCKET_URI"]

LOCAL_DATA_PATH = "raw_data"
LOCAL_REGISTRY_PATH =  "pneumonia/training_weights"
