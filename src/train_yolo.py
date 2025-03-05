from ultralytics import YOLO

def train_model():
    model = YOLO("yolov8n.yaml")  
    model.train(
        data="dataset/data.yaml", 
        epochs=100,
        imgsz=640,
        batch=16,
        name="elderlyaid_model",
        device='cpu'
    )
    print("Training Completed!")

if __name__ == "__main__":
    train_model()
