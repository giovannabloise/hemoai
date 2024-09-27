from setuptools import setup, find_packages

setup(
    name='hemoai',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'click',
        'tensorflow',
        'Pillow',
        'keras'
    ],
    entry_points={
        "console_scripts": [
            'hemoai=hemoai.scripts.main:main',
        ],
    },
)
