from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name='IDC classification',
version='0.0.1',
author='Amzad hossain rafi , Al musabbir rakin ,Afridy ',
author_email='amzad.rafi@northsouth.edu',
package_dir={"": "src"},
packages=find_packages(where="src"),
install_requires=get_requirements('requirements.txt')

)