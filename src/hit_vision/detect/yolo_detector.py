"""YOLO detection module."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List, Dict, Any

from ultralytics import YOLO


@dataclass
class Detection:
    label: str
    confidence: float
    xyxy: List[float]


class YoloDetector:
    """Thin wrapper around Ultralytics YOLO for inference."""

    def __init__(self, model_path: str = "yolov8n.pt") -> None:
        self.model_path = model_path
        self.model = YOLO(model_path)

    def predict(self, source: str | Iterable, conf: float = 0.25) -> List[Detection]:
        """Run detection on an image path or frame (numpy array)."""
        results = self.model.predict(source=source, conf=conf, verbose=False)
        if not results:
            return []

        detections: List[Detection] = []
        r = results[0]
        names = r.names or {}
        boxes = r.boxes
        if boxes is None:
            return []

        for b in boxes:
            cls_id = int(b.cls)
            label = names.get(cls_id, str(cls_id))
            detections.append(
                Detection(
                    label=label,
                    confidence=float(b.conf),
                    xyxy=[float(v) for v in b.xyxy[0].tolist()],
                )
            )
        return detections


def detections_to_dict(detections: List[Detection]) -> List[Dict[str, Any]]:
    """Serialize detections for downstream processing or logging."""
    return [
        {
            "label": d.label,
            "confidence": d.confidence,
            "xyxy": d.xyxy,
        }
        for d in detections
    ]
