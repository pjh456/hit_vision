"""Detection module."""
from .yolo_detector import Detection, YoloDetector, detections_to_dict

__all__ = ["Detection", "YoloDetector", "detections_to_dict"]
