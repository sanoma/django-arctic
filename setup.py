from setuptools import setup, find_packages


__VERSION__ = '0.9.0'

try:
    README = open('README.md').read()
except:
    README = None

try:
    REQUIREMENTS = open('requirements.txt').read()
except:
    REQUIREMENTS = None

setup(
    name='django-arctic',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Internet :: WWW/HTTP',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    version=__VERSION__,
    long_description=README,
    install_requires=REQUIREMENTS,
    packages=find_packages(),
    license='MIT',
    url='https://github.com/sanoma/django-arctic',
    author='Sanoma Netherlands',
    author_email='opensource@sanoma.com',
    description="Django framework to create custom content management systems.",
)
