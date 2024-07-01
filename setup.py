from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."
def get_requirements(find_path:str)->List[str]:
    '''
        this function will return list of requirements
    '''
    requirements = []
    with open(find_path) as file_obj:
        requirements = file_obj.readlines()
        [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        
    return requirements

setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Kanishka',
    author_email = 'kanishkachathu16805@gmail.com',
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')
    
)