"""Text formatting utilities for detection results."""
from __future__ import annotations

from typing import Iterable, List

from hit_vision.detect import Detection


def format_detection(d: Detection) -> str:
    """Format a single detection into a readable string."""
    x1, y1, x2, y2 = d.xyxy
    return f"{d.label} ({d.confidence:.2f}) at [{x1:.0f},{y1:.0f},{x2:.0f},{y2:.0f}]"


def format_detections(detections: Iterable[Detection]) -> str:
    """Format multiple detections into a sentence-like string."""
    items: List[str] = [format_detection(d) for d in detections]
    if not items:
        return "No obstacles detected."
    return "Detected: " + "; ".join(items) + "."
