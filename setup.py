import os

from setuptools import setup, find_packages

with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.md'), encoding='utf-8') as fh:
    long_description = '\n' + fh.read()

setup(
    name='py-okx-async',
    version='1.5.0',
    license='Apache-2.0',
    author='SecorD',
    description='',
    long_description_content_type='text/markdown',
    long_description=long_description,
    packages=find_packages(),
    install_requires=[
        'aiohttp', 'aiohttp-socks', 'pretty-utils @ git+https://github.com/SecorD0/pretty-utils@main', 'PySocks',
        'python-dotenv', 'requests'
    ],
    keywords=[
        'okx', 'pyokx', 'py-okx', 'okxpy', 'okx-py', 'api', 'okxapi', 'okx-api', 'api-okx', 'async-okx',
        'pyokxasync', 'py-okx-async', 'asyncokxpy', 'async-okx-py', 'asyncokxapi', 'async-okx-api'
    ],
    classifiers=[
        'Programming Language :: Python :: 3.8'
    ]
)
