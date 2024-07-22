from setuptools import setup
import os

setup(
    name='file-extension-modifier',
    version='0.3.0', # Remember to increment in __init__.py
    description='A user-friendly Python script for batch-modifying file extensions in a given directory.',
    long_description=open('README.md').read() if os.path.exists('README.md') else '',
    url='https://github.com/Dan-Foord/file-extension-modifier',
    author='Dan-Foord',
    author_email='160248692+Dan-Foord@users.noreply.github.com',
    license='MIT',
    packages=['file_extension_modifier'],
    entry_points = {
        'console_scripts': [
            'file-extension-modifier = file_extension_modifier.__main__:main',
        ],
    },
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License'
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.6',
)