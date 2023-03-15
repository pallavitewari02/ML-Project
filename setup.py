from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT="-e ."
def get_requirements(file_path:str)->List[str]:
    '''
     This function returns the list of  requirements

    '''

    requiremets=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements= [req.replace("\n","")for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements



setup(
name='MLProject',
version='0.0.1',
author='pallavitewari02',
author_email='pallavics2004@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')


)