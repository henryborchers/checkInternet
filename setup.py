from setuptools import setup

setup(
    name='CheckInternet',
    version='0.1.2',
    packages=['checkInternet'],
    url='',
    license='',
    author='Henry Borchers',
    author_email='',
    description='Checks to see if the internet is still accessible and let\'s you know if you know if it goes down',
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'checkinternet = checkInternet.__main__:main'
        ]
    }
)
