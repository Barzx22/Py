from setuptools import setup, find_packages

setup(
    name="pyhelper",
    version="1.0",
    packages=find_packages(),
    install_requires=["black"],
    author="Akbar Maulana",
    description="Library untuk membantu perkodingan Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/username/pyhelper", 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Copyright by ayaka shinjuki",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
