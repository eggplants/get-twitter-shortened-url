from setuptools import find_packages, setup

from t_co import __version__

setup(
    name='t_co',
    version=__version__,
    description='Get shortened link from Twitter URL Shortener (t.co)',
    description_content_type='',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/eggplants/get-twitter-shortened-url',
    author='eggplants',
    packages=find_packages(),
    python_requires='>=3.5',
    include_package_data=True,
    license='MIT',
    install_requires=open('requirements.txt').read().splitlines(),
    entry_points={
        'console_scripts': [
            't_co=t_co.main:main'
        ]
    },
    classifiers=[
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only"
    ]
)
