# !/usr/bin/env python

from distutils.core import setup
import os
import re

wordList = []
with open(os.path.join(os.path.dirname(__file__), 'Pipfile')) as f:
    li = list(f)
    start = li.index('[dev-packages]\n')+1
    end = li.index('[requires]\n')-1

    for item in li[start:end]:
        i = re.sub(' = ', '', item)
        i = re.sub('"', '', i)
        i = re.sub('\*', '', i)
        i = re.sub(r'"(.*)"', r'\1', i)
        wordList.append(i[:-1])
requirements = wordList

setup(
    name='cookiecutter-pypackage',
    packages=[],
    version='0.1.0',
    description='Cookiecutter template for a Python package',
    author='Elien Valleau',
    license='BSD',
    author_email='ev@hubstairs.com',
    url='https://github.com/elienvalleau/cookiecutter-pypackage',
    keywords=['cookiecutter', 'template', 'package', ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development',
    ],
)

