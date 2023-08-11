from setuptools import find_packages,setup
from typing import List

Hypehen_dot = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements] #readlines function will add /n from the txt file
        if Hypehen_dot in requirements:
            requirements.remove(Hypehen_dot)

    return requirements


setup(
name='mlproject',
version='0.0.1',
author='harikrish242',
author_email='harikrish242@gmail.com',
packages=find_packages(),
install_requires = get_requirements('requirements.txt')
)