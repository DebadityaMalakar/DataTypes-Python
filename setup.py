from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Custom Data Tpes'
LONG_DESCRIPTION = 'Custom Data Types in Python'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="cdatatypes", 
        version=VERSION,
        author="Debaditya Malakar",
        author_email="debadityamalakar@outlook.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=["bitstring>=4.0.1"], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)