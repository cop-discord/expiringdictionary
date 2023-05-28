from setuptools import setup


setup(
    name="expiringdictionary",
    version="0.0.1",
    description="a very simple yet very efficient way of making expiring dictionaries and doing ratelimiting",
    long_description="...",
    long_description_content_type="text/markdown",
    url="https://github.com/cop-discord/expiringdictionary",
    author="cop-discord",
    author_email="z@rival.rocks",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent",
        "Typing :: Typed",
    ],
    install_requires=['typing'],
    python_requires=">=3.6",
)
