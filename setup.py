from setuptools import setup

def parse_requirements(filename):
    with open(filename) as f:
        return f.read().splitlines()

setup(
    name="inventory-computostore",
    version="0.0.1",
    description="Aplicación de gestión de inventarios",
    author="fmarinoa",
    packages=["app"],
    install_requires=parse_requirements("requirements.txt"),
)