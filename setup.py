# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


with open("README.md") as f:
    readme = f.read()


setup(
    name='vlcclient',
    version='0.1.0',
    description="Control VLC instances using python.",
    long_description=readme,
    license='BSD',
    url="https://github.com/DerMitch/py-vlcclient",
    author='Michael Mayr',
    author_email='michael@michfrm.net',
    py_modules=['vlcclient'],
    scripts=["vlcclient.py"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
    ],
)
