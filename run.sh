# activate virtual environment
source ./env/bin/activate

# unzip to create emissions folder
unzip emissions.zip

# run code with default argument
python3 src/visualize.py

# deactivate virtual environment
deactivate