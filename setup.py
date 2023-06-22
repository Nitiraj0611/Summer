from setuptools import find_packages,setup
from typing import List

constant = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This will return the list of requiremnets
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ") for req in requirements ]

        if constant in requirements:
            requirements.remove(constant)

    return requirements                  


setup(
    name='Insurance_Premium',
    version='0.0.1',
    author='Nitiraj Singh Chouhan',
    author_email='2020umt1352@mnit.ac.in',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)