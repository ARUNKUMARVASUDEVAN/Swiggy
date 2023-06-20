from setuptools import find_packages,setup
from typing import List
Hyphen_e_dot='-e .'
def get_requirements(file_path):
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readline()
        [req.replace("\n","")for req in requirements]

        if Hyphen_e_dot in requirements:
            requirements.remove(Hyphen_e_dot)
    return requirements
setup(
      name='Regression Assignment',
      version='0.0.1',
      author='arun',
      install_requires=get_requirements('requirements.txt'),
      packages=find_packages()
)