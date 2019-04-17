from setuptools import setup

setup(
    name = 'quran-cli',
    version = '0.1.0',
    packages = ['qurancli'],
    entry_points = {
        'console_scripts': [
            'quran-cli = qurancli.__main__:cli'
        ]
    })
