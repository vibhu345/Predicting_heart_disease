from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT="-e."
def get_requirements(file_path:str)-> List[str]:
    requirements=[]
    with open (file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements= [i.replace("\n"," ") for i in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    author='Vibhanshu Gupta',
    author_email="vibhanshugupta875@gmail.com",
    name="Heart Disease prediction project",
    install_requires=get_requirements("requirements.txt"),
    packages=find_packages(),
    version="0.0.0.1"

)