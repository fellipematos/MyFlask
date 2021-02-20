from setuptools import find_packages, setup


def read(filename):
    return [req.strip() for req in open(filename).readlines()]

setup(
    name="myflask",
    version="0.0.0",
    description="MyFlask Base",
    packages=find_packages(),
    include_package_data=True,
    install_requires=read("requirements.txt"),
    extras_require={"dev": read("requirements-dev.txt")}
)
