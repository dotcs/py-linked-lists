from setuptools import setup, find_packages
from pathlib import Path

deps = Path("requirements.txt").read_text("utf-8").splitlines()

setup(
    name="linked-list",
    version="0.0.0",
    url="https://github.com/dotcs/py-linked-lists",
    author="Fabian Mueller",
    author_email="packages@dotcs.me",
    description="Description of my package",
    packages=find_packages(),
    install_requires=deps,
)