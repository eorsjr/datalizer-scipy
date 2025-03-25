from setuptools import setup, find_packages

setup(
    name='datalizer',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy'
    ],
    author="Eörs Szathmáry, Péter Osztobányi, Réka Kovács",
    url="https://github.com/eorsjr/datalizer-scipy",
    description="Datalizer - A Python package for cleaning and preprocessing datasets.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)