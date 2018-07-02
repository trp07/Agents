import ast
import re
from setuptools import setup, find_packages


# get __version__ from __init__.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')
with open('agentpy/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))


# load README.md
with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()


setup(
    name='agentpy',
    version=version,
    url='https://github.com/trp07/Agents',

    description=('A recreation of the python source repository'
        ' for Artificial Intelligence: A Modern Approach'),
    long_description=readme,
    long_description_content_type='text/markdown',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Agent Systems',
    ],

    python_requires='>=3.5',

    test_suite='tests',
    test_requires=[
        'pytest-cov',
        'pytest-mock',
    ],

    setup_requires=['pytest-runner'],
)
