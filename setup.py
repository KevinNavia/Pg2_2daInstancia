import setuptools
from pathlib import Path

# Read the README file for the long description
this_directory = Path(__file__).parent
long_description = ""
readme_path = this_directory / "README.md"
if readme_path.is_file():
    long_description = readme_path.read_text(encoding="utf-8")

setuptools.setup(
    name="minivalidator",
    version="0.1.0",
    author="Tu Nombre",
    author_email="tu-email@example.com",
    description="Pequeña librería de validadores reutilizables.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        # Add any dependencies here if needed
    ],
)
