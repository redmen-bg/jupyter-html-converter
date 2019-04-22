#!/bin/bash

echo "--------------------"
echo "Building lambda"

cd ../ # project root directory

echo "Create dist directory"
pwd
mkdir dist

echo "Create package directory"
pwd
mkdir package

echo "Build the project dependencies"
cd package
pwd
pip install -r ../requirements.txt --target .

echo "Prepare initial archive package"
pwd
zip -r9 ../dist/function.zip .

echo "Add lambda to the archive package"
cd ../
pwd
zip -g dist/function.zip *.py
