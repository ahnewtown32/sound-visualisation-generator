# sound-visualisation-generator
A desktop tool that analyses an audio file and produces an audio-reactive Perlin noise video, with live controls for mapping bass/mids/highs to visual parameters

## Overview

This project aims to create a simple application that takes an audio WAV file and generates a Perlin noise–based video that reacts to the sound. Users can adjust settings that influence how audio features (bass, mids, highs) are mapped to visual parameters such as scale, speed, colour, and detail.

While there are existing open-source audio visualisers available online, many are complex to set up, feature-heavy, and have a steep learning curve. Our goal is to keep the UI lightweight and easy to use, with a small set of clear controls focused on producing good-looking results quickly.

The output of the application is an MP4 video containing the generated Perlin noise visualisation.

## Target Users

This project is aimed at content creators, musicians, and anyone interested in generating visuals that react to audio.

## Requirements

- Python 3.8+
- FFmpeg (required for video encoding)

## Installation

```bash
# Clone the repository
git clone https://github.com/ahnewtown32/sound-visualisation-generator.git
cd sound-visualisation-generator

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

> **Note:** Full usage instructions will be added once the CLI/UI entrypoint is finalized.

Basic usage:
```bash
python main.py --input your_audio.wav --output visualization.mp4
```

## Tech Stack

- **Python 3.8+** - Core programming language
- **NumPy** - Numerical computations
- **librosa** - Audio analysis and feature extraction
- **OpenCV** - Video generation and export
- **noise** - Perlin noise generation
- **FFmpeg** - Video encoding

## Project Structure

```
sound-visualisation-generator/
├── src/
│   ├── audio/          # Audio analysis modules
│   ├── visual/         # Perlin noise generation
│   ├── export/         # Video rendering and export
│   └── ui/             # User interface components
├── tests/              # Unit and integration tests
├── examples/           # Sample audio files and outputs
├── docs/               # Documentation and assets
├── requirements.txt    # Python dependencies
├── CONTRIBUTING.md     # Contribution guidelines
├── LICENSE             # License information
└── README.md           # This file
```

## Roadmap

- [ ] Basic audio analysis (bass/mids/highs detection)
- [ ] Perlin noise generation
- [ ] Video export to MP4
- [ ] Basic GUI 
- [ ] Parameter adjustment


## Contributing

Contributions are welcome! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details on how to get started.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Support

If you encounter any issues or have questions:
- Check existing [Issues](https://github.com/ahnewtown32/sound-visualisation-generator/issues)
- Open a new issue using our templates
- Reach out via [GitHub Discussions](https://github.com/ahnewtown32/sound-visualisation-generator/discussions)
