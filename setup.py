from setuptools import setup

setup(
    name = 'dson',
    version = '0.1.0',
    py_modules = ['dson'],
    description = 'Like bson, \'cept different.',
    author = 'Elisha Fitch-Cook',
    author_email = 'elisha@elishacook.com',
    url = 'https://github.com/elishacook/dson',
    test_suite = 'tests',
    install_requires=['pytz']
)
