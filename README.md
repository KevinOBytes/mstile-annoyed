# mstile-annoyed

[![PyPI version](https://badge.fury.io/py/mstile-annoyed.svg)](https://badge.fury.io/py/mstile-annoyed)
[![Test](https://github.com/KevinOBytes/mstile-annoyed/actions/workflows/test.yml/badge.svg)](https://github.com/KevinOBytes/mstile-annoyed/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/KevinOBytes/mstile-annoyed/branch/main/graph/badge.svg)](https://codecov.io/gh/KevinOBytes/mstile-annoyed)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Versions](https://img.shields.io/pypi/pyversions/mstile-annoyed.svg)](https://pypi.org/project/mstile-annoyed/)

A powerful Python utility for generating Microsoft Tile (mstile) PNG icons for NextJS 15 web applications - really for any web application or website. This tool simplifies the process of creating properly sized and formatted icons for Windows pinned sites and applications.

## Features

- 🎯 Generates all standard mstile icon sizes in one command
- 🖼️ Maintains aspect ratio while resizing
- 🎨 Preserves transparency and image quality
- 📐 Centers images automatically with proper padding
- 🚀 Easy to use CLI and Python API
- 🔧 High-quality Lanczos resampling

## Installation

### Using pip (Recommended)

```bash
pip install mstile-annoyed
```

### From source

```bash
git clone https://github.com/KevinOBytes/mstile-annoyed.git
cd mstile-annoyed
pip install -e .
```

## Quick Start

### Command Line Interface

Generate all mstile icons with a single command:

```bash
mstile-annoyed generate logo.png --output-dir public/icons
```

### Python API

```python
from mstile_annoyed.core import generate_mstile_icons

# Generate all icon sizes
generated_files = generate_mstile_icons('logo.png', 'public/icons')

# Print generated file paths
for file in generated_files:
    print(f"Generated: {file}")
```

## Generated Icons

The tool generates the following standard mstile icon sizes:

| Filename | Dimensions | Use Case |
|----------|------------|----------|
| mstile-70x70.png | 70×70 | Small tile |
| mstile-144x144.png | 144×144 | Medium tile |
| mstile-150x150.png | 150×150 | Medium tile (alternative) |
| mstile-310x310.png | 310×310 | Large tile |
| mstile-310x150.png | 310×150 | Wide tile |

## Integration with NextJS

Add the following to your `app/layout.tsx` or equivalent:

```html
<link rel="msapplication-square70x70logo" content="/icons/mstile-70x70.png" />
<link rel="msapplication-square144x144logo" content="/icons/mstile-144x144.png" />
<link rel="msapplication-square150x150logo" content="/icons/mstile-150x150.png" />
<link rel="msapplication-square310x310logo" content="/icons/mstile-310x310.png" />
<link rel="msapplication-wide310x150logo" content="/icons/mstile-310x150.png" />
```

## Advanced Usage

### Custom Output Directory

```bash
mstile-annoyed generate logo.png --output-dir custom/path/icons
```

### Programmatic Usage with Custom Error Handling

```python
from pathlib import Path
from mstile_annoyed.core import generate_mstile_icons

try:
    output_dir = Path("public/icons")
    files = generate_mstile_icons("logo.png", output_dir)
    print(f"Successfully generated {len(files)} icons")
except FileNotFoundError:
    print("Error: Input file not found")
except Exception as e:
    print(f"Error generating icons: {str(e)}")
```

## Development

### Setting Up Development Environment

```bash
# Clone the repository
git clone https://github.com/KevinOBytes/mstile-annoyed.git
cd mstile-annoyed

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements.txt
```

### Running Tests

```bash
pytest
```

### Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Requirements

- Python 3.8+
- Pillow library for image processing
- Click for CLI interface

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Kevin O'Connor ([@KevinOBytes](https://github.com/KevinOBytes))

## Acknowledgments

- Inspired by the need for automated mstile icon generation in NextJS projects
- Built with [Pillow](https://python-pillow.org/) for high-quality image processing
- CLI powered by [Click](https://click.palletsprojects.com/) 

## Disclaimer 

This project was developed with the assistance of large language models. I'm not a professional software developer, but a security guy - so use this tool at your own risk. 