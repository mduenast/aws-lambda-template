from setuptools import setup, find_packages

with open('requirements.txt') as file:
    requirements = file.read().splitlines()

setup(
    name="aws-lambda",
    version="1.0.0-ALPHA",
    packages=find_packages(include=["src", "src.*"]),
    install_requires=requirements,
    include_package_data=True,

    # Metadata
    author="mduenast",
    author_email="user@mail.com",
    description="A simple script to be run on AWS Lambda",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="http://example.com/yourprojectname",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Python Software Foundation License',
        'Programming Language :: Python :: 3',
        'Environment :: AWS :: LAMBDA',
    ],
)