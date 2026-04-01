"""TTS utilities.

This module provides a minimal interface for local TTS.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass
class TtsResult:
    text: str
    output_path: Path


def synthesize(text: str, output_path: str | Path, voice: Optional[str] = None) -> TtsResult:
    """Generate speech audio from text.

    Note: This is a placeholder implementation. Integrate a concrete TTS engine
    (e.g., KittenTTS or Qwen3-TTS) in a later step.
    """
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Placeholder: create an empty file as a stub artifact.
    output_path.write_bytes(b"")

    return TtsResult(text=text, output_path=output_path)
