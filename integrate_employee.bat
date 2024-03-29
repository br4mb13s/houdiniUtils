::!/bin/bash

::system integration step
python system_integration.py

::create user data package
python create_package_json.py

::copy package file into Houdini
copy packages\company_vars.json C:\Users\Joshua\Documents\houdini20.0\packages

echo "All steps done!"