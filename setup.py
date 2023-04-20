#!/usr/bin/env python3 -i

## Written using Python version 3.7.
## Written on 27FEB2019.
## Last modified 29AUG2022.
## Adheres to PEP 8 standard of 72 character comment length limits.
## https://www.python.org/dev/peps/pep-0008/
## General line limit is 120 characters.
## This script was written by Raymond Carlson.
## Email: raymondac@buildingmoc.com
## Phone Number: 559-260-4506
## This script is the property of Building Maintenance Optimization
##  Consultants, Inc. (BMOC)
## 4426 Hugh Howell Road Suite B 138, Tucker, GA 30084
## Office Phone Number: 877-574-4313
## This script is for the exclusive use by BMOC.
## All other uses of this script are prohibited without advance
## , express, written consent of BMOC.
## This file is a living document meant to consolidate the various
## scripts written for BMOC in its operations and to make them more 
## useable for the entirety of the company.

import setuptools 
## https://setuptools.readthedocs.io/en/latest/setuptools.html

setuptools.setup(
                 name = 'st_aggrid_bmoc'
                 , version = '0.0.5'
                 , author = 'Raymond Carlson'
                 , author_email = 'raymondac@buildingmoc.com'
                 , description = 'Various Tools for use with BMOC Data'
                 , long_description = 'Please fill me out one day.'
                 , long_description_content_type = 'text'
                 , url = 'https://www.buildingmoc.com/'
                 , packages = setuptools.find_packages()
                 , classifiers = [
                                 'Programming Language :: Python :: 3 :: Only'
                                 , 'Environment :: Console'
                                 , 'License :: Other/Proprietary License'
                                 , 'Operating System :: OS Independent'
                                 , 'Development Status :: 2 - Pre-Alpha'
                                 , 'Natural Language :: English'
                                 ] #See https://pypi.org/classifiers/
                 , license = 'proprietary'
                 , python_requires = '>=3.7'
                 , package_data={'': ['.env', '.prettierrc', '*.css', '*.html', '*.js', '*.json', '*.map', '*.txt', '*.woff', '*.woff2']}
                 , include_package_data=True
                 )
