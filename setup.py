import os
import re

from setuptools import setup
from setuptools import find_packages

ROOT = os.path.dirname(__file__)
VERSION_RE = re.compile(r"""__version__ = ['"]([0-9.]+)['"]""")


def get_version():
    init = open(os.path.join(ROOT, "lamblayer", "__init__.py")).read()
    return VERSION_RE.search(init).group(1)


setup(
    name="lamblayer",
    version=get_version(),
    description="a minimal deployment tool for AWS Lambda layers",
    author="Yusuke Takahashi",
    author_email="takahashi@adansons.co.jp",
    packages=find_packages("lamblayer"),
    install_requires=["boto3", "click"],
    entry_points={"console_scripts": ["lamblayer=lamblayer.cli:main"]},
)
