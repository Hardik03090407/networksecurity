'''
This is a setup.py file for a Python package. It uses setuptools to define the package metadata and dependencies.
'''

from setuptools import setup,find_packages
from typing import List

def get_requirements()->List[str]:
    '''
    This function is used to fetch the list of requirementa
    '''
    requirement_lst:List[str]=[]
    try:
        with open("requirements.txt",'r') as file:
            # we will read lines from the file
            lines=file.readlines()
            # removing newline characters and extra spaces
            for line in lines:
                requirement=line.strip()
                # ignoring .e 
                if requirement and requirement!=".e":
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

print(get_requirements())

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Hardik Rawat",
    author_email="hardikrawat79@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)