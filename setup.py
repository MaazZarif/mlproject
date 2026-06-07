from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    with open(file_path, encoding="utf-8-sig") as file_obj:
        requirements = file_obj.readlines()

    requirements = [req.strip() for req in requirements if req.strip()]

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name="mlproject",
    version="0.0.1",
    author="Maaz",
    author_email="maazbangash2004@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)