from setuptools import find_packages,setup
from typing import List

hyphon_dot="-e ."
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("/n","") for req in requirements]

        if hyphon_dot in requirements:
            requirements.remove(hyphon_dot)

        return requirements

setup(
    name='Test_for_upload',
    version='0.0.1',
    author='Swapnil Sutar',
    install_requires=get_requirements('requirement.txt'),
    packages=find_packages()
)