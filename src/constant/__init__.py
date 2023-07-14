import os


AWS_S3_BUCKET_NAME = "wafer-fault"

DATABASE_NAME="waferfault_detection_database"
COLLECTION_NAME="waferfault_data"

TARGET_COLUMN = "quality"
MONGO_DB_URL=uri = "mongodb+srv://hellokunal:Wafer@cluster0.hrdp8gn.mongodb.net/?retryWrites=true&w=majority"

MODEL_FILE_NAME = "model"
MODEL_FILE_EXTENSION = ".pkl"

artifact_folder =  "artifacts"