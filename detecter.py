from ultralytics import YOLO
import cv2
 #モデルの読み込み
model = YOLO("yolov8n.pt")
# 画像の読み込み
img = cv2.imread("bus.jpg")

results = model(img)
annoted_frame = results[0].plot()

cv2.imshow("YOLOv8 Detection", annoted_frame)
cv2.waitKey(0)
cv2.destroyAllWindows()