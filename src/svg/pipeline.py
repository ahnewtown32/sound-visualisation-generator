from __future__ import annotations

from pathlib import Path


def generate_visualization(input_path: str, output_path: str) -> Path:
    """
    Temporary placeholder. Creates an output file so CI can validate plumbing.
    Replace with real audio->video pipeline later.
    """
    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(b"placeholder mp4 bytes")
    return out
