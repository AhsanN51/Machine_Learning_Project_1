from setuptools import setup, find_packages

HYPEN = "-e ."


def get_requirements(file_path):

    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN in requirements:
            requirements.remove(HYPEN)

    return requirements


setup(
    name="mlproject",
    version="0.0.1",
    author="Ahsan",
    author_email="muhammadahsan8013@gmail.com",
    packages=find_packages(),
    install_requirments=get_requirements("requirements.txt"),
)
