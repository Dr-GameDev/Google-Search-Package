from setuptools import setup

with open("../README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='search-terminal',
    version='0.0.2',
    author="Babalo Majiyezi",
    author_email="raymondbabalo5@gmail.com",
    description="This is a program that allows you to search the web from the comfort of your terminal.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["search_package"], 
    url="https://github.com/Dr-GameDev/Google-Search-Package",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'argparse',
        'requests',
        'html2text',
    ],
    entry_points={
        'console_scripts': [
            'search = search_package.search:main', 
        ],
    },
    keywords=["search", "web search", "terminal search"],
    license="MIT",
)
