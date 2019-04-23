#!/bin/bash

echo "--------------------"
echo "Building lambda"

cd ../ # project root directory

echo "Create dist directory"
pwd
mkdir dist

echo "Create a virtual environment"
virtualenv lambda-env

echo "Activate the environment"
source ./lambda-env/bin/activate

echo "Install dependency libraries"
printf "%s\n" $IPYTHONDIR
pip3 install -r requirements.txt && \
  cp -r /var/lang/bin .

echo "kernelspec list"
jupyter kernelspec list

echo "list.."
ls -la /var/jenkins_home/workspace/jupyter-html-converter/lambda-env/share/jupyter/kernels/python3
ls -la /var/task/

echo "Set up Jupyter Python3 kernel"
# python3 -m ipykernel install
# ipython kernel install
# python -m ipykernel install --sys-prefixs
# python -m ipykernel install --prefix .

echo "Deactivate the virtual environment."
deactivate

echo "Setting python path"
export PYTHONPATH="/var/task"
echo "$PYTHONPATH"

export IPYTHONDIR='/tmp/ipythondir'
echo "$IPYTHONDIR"

echo "Prepare initial archive package"
cd lambda-env/lib/python3.7/site-packages/
pwd
zip -r9 ../../../../dist/function.zip .

echo "Add lambda to the archive package"
cd ../../../../
pwd
zip -g dist/function.zip *.py
