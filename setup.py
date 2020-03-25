from setuptools import setup

setup(
    name = 'quran-cli',
    version = '0.1.0',
    packages = ['qurancli'],
    install_requires = ['prettytable==0.7.2', 'requests==2.20.0', 'Click==7.0'],
    entry_points = {
        'console_scripts': [
            'quran-cli = qurancli.__main__:cli'
        ]
    })
