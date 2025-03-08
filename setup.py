from setuptools import setup, find_packages
import os

# Read the contents of README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read version from __init__.py
with open(os.path.join("mstile_annoyed", "__init__.py"), "r") as f:
    for line in f:
        if line.startswith("__version__"):
            version = line.split("=")[1].strip().strip('"').strip("'")
            break

setup(
    name="mstile-annoyed",
    version=version,
    author="Kevin O'Connor",  # TODO: Update with your name
    author_email="kevin@kevinbytes.com",  # TODO: Update with your email
    description="A Python utility for generating Microsoft Tile (mstile) PNG icons for NextJS applications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KevinOBytes/mstile-annoyed",  # TODO: Update with your repository URL
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "Pillow>=10.2.0",
        "click>=8.1.7",
    ],
    entry_points={
        "console_scripts": [
            "mstile-annoyed=mstile_annoyed.__main__:cli",
        ],
    },
) 