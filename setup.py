#  <!-- this file can help to serve you project as a package -->
from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT="-e."
def get_requirement(file_path:str)-> List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements_list=[]
    with open (file_path) as file_obj:
        requirements_list=file_obj.readlines()
        requirements_list=[i.replace("\n"," ")for i in requirements_list]
        if HYPEN_E_DOT in requirements_list:
            requirements_list.remove(HYPEN_E_DOT)
    return requirements_list


setup(
    name="ML PROJECT",
    version="0.01",
    author="Vibhanshu",
    author_email="vibhanshugupta875@gmail.com",
    packages=find_packages(),
    install_requirements= get_requirement("requirements.txt")
)