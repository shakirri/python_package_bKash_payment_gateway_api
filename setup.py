from setuptools import find_packages, setup

long_description = "long"

setup(
    name="bKashpgw",
    version="0.0.4",
    description="a payment gateway api package for bKash",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ArjanCodes/2023-package",
    author="Redwanul Islam Shakir",
    author_email="ri8shakir@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests >= 2.31.0"],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],
    },
    python_requires=">=3.10",
)