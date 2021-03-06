from setuptools import setup
import sys

depends = []
if sys.platform == "darwin":
    depends.append("pyobjc")

setup(
    name='CheckInternet',
    version='0.2.10',
    packages=['checkInternet', 'checkInternet.Alerts'],
    url='',
    license='',
    author='Henry Borchers',
    author_email='',
    scripts=['scripts/cli.py'],
    install_requires=depends,
    description='Checks to see if the internet is still accessible and let\'s you know if you know if it goes down',
    zip_safe=False,
    test_suite="nose.collector",
    tests_require=['nose'],
    entry_points={
        'console_scripts': [
            'checkinternet = scripts:main'
        ]
    }
)
