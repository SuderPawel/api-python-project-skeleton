# coding=utf-8
# !/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    print 'No setuptools installed, use distutils'
    from distutils.core import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='api-python-project-skeleton',
    packages=[
        'api_python_project_skeleton',
        'api_python_project_skeleton.tools',
        'api_python_project_skeleton.tests'
    ],
    package_dir={
        'api_python_project_skeleton': 'src/api_python_project_skeleton',
        'api_python_project_skeleton.tools': 'src/api_python_project_skeleton/tools',
        'api_python_project_skeleton.tests': 'src/api_python_project_skeleton/tests'
    },
    package_data={'': [
        'src/api_python_project_skeleton/main.ini',
        'src/api_python_project_skeleton/api.ini'
    ]},
    data_files=[
        ('', [
            'src/api_python_project_skeleton/main.ini',
            'src/api_python_project_skeleton/api.ini'
        ]),
    ],
    test_suite="api_python_project_skeleton.tests",
    include_package_data=True,
    install_requires=required,
    version='1.0',
    description='API python project skeleton',
    author=u'Paweł Suder',
    author_email='pawel@suder.info',
    url='https://github.com/your-name/api-python-project-skeleton',
    download_url='https://github.com/your-name/api-python-project-skeleton',
    keywords=[
        'skeleton'
    ],
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    long_description='''\
'''
)
