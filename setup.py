from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="cleberity_detection_and_qa_system",
    version="0.1",
    author="HasanTugraAykac",
    packages=find_packages(),
    install_requires = requirements,
)