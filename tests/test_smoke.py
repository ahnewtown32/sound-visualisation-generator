from pathlib import Path

from svg.pipeline import generate_visualization


def test_generate_visualization_creates_output(tmp_path: Path) -> None:
    input_wav = tmp_path / "in.wav"
    input_wav.write_bytes(b"fake wav")  # placeholder for now

    output_mp4 = tmp_path / "out.mp4"
    generate_visualization(str(input_wav), str(output_mp4))

    assert output_mp4.exists()
    assert output_mp4.stat().st_size > 0
