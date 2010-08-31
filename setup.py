#!/usr/bin/env python
try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages


setup(
    name='ansi2html',
    version='0.2',
    description="Python Wrapper for pixelbeat.org's ansi2html.sh"
    long_description=open('README.md').read(),
    author='Ralph Bean',
    author_email='ralph.bean@gmail.com',
    url='http://github.com/ralphbean/ansi2html/',
    install_requires=[
        "genshi",
    ],
    packages=['ansi2html'],
    scripts=['ansi2html'],
)

from distutils.core import setup

setup(name='ansi2html',
      version='0.2',
      description="Python Wrapper for pixelbeat.org's ansi2html.sh"
      author='Ralph Bean',
      author_email='ralph.bean@gmail.com',
      url='http://github.com/ralphbean/ansi2html/'
      packages=['ansi2html',],
      scripts=['ansi2html'],
     )

