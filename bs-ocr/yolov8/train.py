from ultralytics import YOLO

# Load a model
# model = YOLO("yolov8n.yaml")  # build a new model from scratch
model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

# Use the model
model.train(data="/Users/roshanbisht/Documents/code/bs-ocr/data/train_data_yolo_format_CR/dataset.yaml", epochs=3)  # train the model