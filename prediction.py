from ultralytics import YOLO
from roboflow import Roboflow
import cv2
import supervision as sv
import numpy as np
import torch

# rf = Roboflow(api_key="7tmllls4BTvoWMy9lAy7")
# project = rf.workspace().project("plants-images")
# model = project.version(8).model
# project = rf.workspace().project("deforestation-p5ehc")
# model = project.version(1).model

# torch.save(model, 'model.pt')

# model = YOLO('yolov8n.pt')
model = YOLO('model.pt')

VIDEO_PATH = 'video.mp4'

results = model.track(source=VIDEO_PATH, show=True, tracker="bytetrack.yaml") 


# byte_tracker = sv.ByteTrack()
# annotator = sv.BoxAnnotator()

# def callback(frame: np.ndarray, index: int) -> np.ndarray:
#     results = model(frame)[0]
#     detections = sv.Detections.from_ultralytics(results)
#     detections = byte_tracker.update_with_detections(detections)
#     labels = [
#         f"#{tracker_id} {model.model.names[class_id]} {confidence:0.2f}"
#        for _, _, confidence, class_id, tracker_id
#       in detections
#    ]
#     return annotator.annotate(scene=frame.copy(), detections=detections, labels=labels)

# sv.process_video(source_path=VIDEO_PATH, target_path=f"result.mp4", callback=callback)

# args = {
#     'confidence':90,
#     'overlap':30
# }

# result = model.predict("plant1.jpeg", **args).save("prediction.jpg")
# print(result)
# print("Result saved successfully in prediction.jpg")
# results = model.track(source=0, conf=0.4, show=True, save=True, \
    # save_txt=True, save_conf=True, save_crop=True, tracker="bytetrack.yaml")
# also botsort.yaml

# print(results)

# import cv2
# import inference
# import supervision as sv
# import os

# os.environ["API_KEY"] = "7tmllls4BTvoWMy9lAy7"

# annotator = sv.BoxAnnotator()

# def on_prediction(predictions, image):
#     labels = [p["class"] for p in predictions["predictions"]]
#     detections = sv.Detections.from_roboflow(predictions)
#     cv2.imshow(
#         "Prediction", 
#         annotator.annotate(
#             scene=image, 
#             detections=detections,
#             labels=labels
#         )
#     ),
#     cv2.waitKey(1)

# inference.Stream(
#     source="webcam", # or rtsp stream or camera id
#     model="plants-images/8", # from Universe
#     output_channel_order="BGR",
#     use_main_thread=True, # for opencv display
#     on_prediction=on_prediction, 
# )