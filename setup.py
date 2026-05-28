from setuptools import setup, find_packages
from typing import List


HYPEN_E_DOT = '-e .'



def get_requirements(file_path:str)->list:
    '''This function will return the list of requirements'''
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements



setup(
    name='mlproject1',
    version='0.0.1',
    packages=find_packages(),
    author='Shivam Saxena',
    author_email="shivamsaxena562006@gmail.com",
    #install_requires=['numpy', 'pandas', 'seaborn']
    install_requires=get_requirements('requirements.txt')
)