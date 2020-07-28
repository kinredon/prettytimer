from setuptools import setup

with open("README.md") as f:
    long_description = f.read()


def local_scheme(version):
    """Skip the local version (eg. +xyz of 0.6.1.dev4+gdf99fe2)
    to be able to upload to Test PyPI"""
    return ""


setup(
    name="prettytimer",
    description=" a sssuper simple yet useful tool for you to collct \
    the running time of the codeblock",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="kinredon",
    author_email="kinredon@163.com",
    maintainer="kinredon",
    url="https://github.com/kinredon/prettytimer",
    project_urls={"Source": "https://github.com/kinredon/prettytimer"},
    license="BSD (3 clause)",
    use_scm_version={"local_scheme": local_scheme},
    setup_requires=["setuptools_scm"],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: BSD License",
        "Topic :: Text Processing",
    ],
    py_modules=["prettytimer"],
)
