import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="metadata_logger",
    version="0.0.1",
    author="Ari Croock",
    author_email="acroock@isaziconsulting.co.za",
    description="A small library that allows arbitrary metadata to be automatically logged and passed around different contexts (e.g. Flask, Celery).\nHeavily based on https://github.com/Workable/flask-log-request-id",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/isaziconsulting/metadata_logger",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires=[],
    extras_require={
        'flask': ['Flask>=0.8'],
        'celery': ['celery~=4.1.0']
    }
)
