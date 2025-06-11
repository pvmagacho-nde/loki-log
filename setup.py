from setuptools import setup, find_packages
import os

# Read the README file for the long description
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="loki-log",
    version="0.1.1",
    author="Paulo Vitor Magacho",
    author_email="paulo@nde.com",
    description="A simple structured Loki compatible logging utility for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pvmagacho-nde/loki-log",
    packages=find_packages(where="."),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Logging",
    ],
    keywords="logging structured-logging python loki",
    python_requires='>=3.6',
    project_urls={
        "Source": "https://github.com/pvmagacho-nde/loki-log",
        "Tracker": "https://github.com/pvmagacho-nde/loki-log/issues",
    },
)

