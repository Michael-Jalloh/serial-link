from setuptools import setup
from os import path
this_directory = path.abspath(path.dirname(__file__))
long_description = ""
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(
    name="serial-link",
    packages=["serial-link"],
    version="0.1",
    license="MIT",
    description="This is a simple library that helps in serial communication between arduino using the link arduino library and a host computer.",
    author="Michael Jalloh",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author_email="michaeljalloh19@gmail.com",
    url="https://github.com/Michael-Jalloh/link",
    download_url="https://github.com/Michael-Jalloh/serial-link/archive/v_0.1.tar.gz",
    keywords=["serial-link","serial","arduino"],
    install_requires=[
        "pyserial"
    ],
    classifiers= [
        "Development Status :: 4 - Beta",      
        "Intended Audience :: Developers",      
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",   
        "Programming Language :: Python :: 3",   
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ]
)