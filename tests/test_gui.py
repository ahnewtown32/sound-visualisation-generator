import os

import pytest

from svg.ui.app import SoundVisualisationApp

pytestmark = pytest.mark.skipif(
    os.environ.get("DISPLAY") is None,
    reason="No display available for Tkinter GUI tests.",
)


def create_app():
    app = SoundVisualisationApp()
    app.withdraw()
    return app


def test_app_creation():
    app = create_app()
    assert app.title() == "Sound Visualisation Generator"
    app.destroy()


def test_default_audio_file():
    app = create_app()
    assert app.audio_file == ""
    app.destroy()


def test_slider_defaults():
    app = create_app()
    assert round(app.scale_slider.get(), 1) == 1.0
    assert round(app.speed_slider.get(), 1) == 1.0
    assert int(app.detail_slider.get()) == 5
    app.destroy()
