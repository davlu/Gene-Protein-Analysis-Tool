from setuptools import setup

setup(
    name='GPA_Tool',
    version='0.0.1',
    py_modules=['analytics'],
    install_requires=[
        'Click',
    ],
    entry_points='''
    [console_scripts]
    gpa-tool=MainAnalysis:main
    ''',
      )
