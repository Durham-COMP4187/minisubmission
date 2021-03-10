from setuptools import find_packages, setup

setup(name="minisubmission",
      version="0.1",
      description="Formative github classroom submission.",
      install_requires=["flake8",
                        "pytest"],
      packages=find_packages())
