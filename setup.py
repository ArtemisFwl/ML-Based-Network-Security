from setuptools import find_packages, setup
from typing import list 

def get_requirements()->List[str]:
    """This function will return list of requirement"""
    try:
        with open('requirements.txt', 'r') as file:
            #Read lines from the file 
            lines=file.readlines()
            #Process each line 
            for line in lines:
                requirement=line.strip()
                

