import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name="IPTODataAPI",
    version="1.0.0",
    author="Andreas Stratis",
    author_email="stratis.andreas@hotmail.com",
    description="Package for accessing the operational and market data of the Greek Independent Power Transmission "
                "Operator (IPTO)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/astratis/IPTODataAPI",
    packages=['IPTODataAPI'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)