
from setuptools import setup, find_packages
from filer.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='filer',
    version=VERSION,
    description='A python CLI tool to manipulate files',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Frederik Madsen',
    author_email='frede.madsen3@gmail.com',
    url='https://github.com/johndoe/myapp/',
    license='unlicensed',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'filer': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        filer = filer.main:main
    """,
)
