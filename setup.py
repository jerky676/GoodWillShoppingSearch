import codecs
import os
import sys

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

__version__ = None
exec(open(f"{here}/GoodWillShoppingSearch/version.py").read())

long_description = ""
with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as readme:
    long_description = readme.read()


validate_dependencies = [
    "pytest>=5.4,<6",
    "flake8>=3,<4",
]

setup(
     # Needed to silence warnings (and to be a worthwhile package)
    name='GoodWillShoppingSearch',
    url='https://github.com/jerky676',
    author='Jerky676',
    author_email='jerky676@gmail.com',
    # Needed to actually package something
    packages=['GoodWillShoppingSearch'],
    # Needed for dependencies
    install_requires=["beautifulsoup4", "unidecode", "requests", "pytz"],
    # *strongly* suggested for sharing
    version='1.0.0',
    # The license can be anything you like
    license='MIT',
    description='An example of a python package from pre-existing code',
    # We will also need a readme eventually (there will be a warning)
    long_description=open('README.md').read(),
     classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic ::  :: Chat",
        "License :: Public Domain",
        "License :: Free for non-commercial use",
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        "Topic :: Shopping",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
    ],
    keywords=["good will", "good will shopping", "good", "will", "shopping", "search"],  
    packages=find_packages(
        exclude=[
            "tests",
            "tests.*",
        ]
    ),
)