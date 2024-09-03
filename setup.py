import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), "README.md")) as f:
    readme = f.read()

setup(
    name="django-wait-for-db",
    version="1.0.1",
    description="Simple Django app that provides a simple command to wait for the database to be ready before starting the server.",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="enzo_frnt",
    author_email="contact@enzo-frnt.fr",
    url="https://github.com/enzofrnt/django_wait_for_db",
    license="MIT",
    zip_safe=False,
    packages=[
        "wait_for_db",
        "wait_for_db.management",
        "wait_for_db.management.commands",
    ],
    install_requires=[
        "Django",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries",
    ],
)