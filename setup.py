from setuptools import setup, find_packages

setup(
    name="simple_image_processing",
    version="0.1",
    packages=find_packages(),
    description="A simple image processing package",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/lucas-ponte-e-silva/simple-package-template",
    install_requires=[
        "numpy",
        "Pillow"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)