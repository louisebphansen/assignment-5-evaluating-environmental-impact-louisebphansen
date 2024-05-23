# assignment-5-evaluating-environmental-impact-louisebphansen

This assignment is the fifth and final assignment for the portfolio exam in the Language Analytics course at Aarhus University, spring 2024.

### Contributions

The code was written by me, but code provided in the notebooks for the course has been reused. 

### Assignment description

For this assignment, I want you to go back to all four of previous assignments in Language Analytics. For each assignment, I want you to use CodeCarbone to measure the environmental impact of your code in terms of CO₂eq. You should specifically address the following questions:

- Which assignment generated the most emissions in terms of CO₂eq? Explain why this might be.
- Which specific tasks generated the most emissions in terms of CO₂eq? Again, explain why this might be.
- How robust do you think these results are and how/where might they be improved?

### Contents of the repository

| <div style="width:120px"></div>| Description |
|---------|:-----------|
| ```out``` | Contains the output plots showing emissions for assignments and subtasks within each assignment|
| ```src```  | Contains the Python scripts for generating plots of emissions for assignments|
| ```run.sh```    | Bash script for running script with default arguments|
| ```setup.sh```  | Bash script for setting up virtual environment|
| ```requirements.txt```  | Packages required to run the code|
|```data.zip```| Zipped datafolder containing all csv files containing information about emissions from running code from Assignments 1-4|

### Methods & Data
This repository contains the code to visualize results from csv files containing information about C02-equivalent emissions from running the code in Assignment 1-4. The csv files are found in the ```data.zip``` file; unzipping it will create the folder ```emissions``` with four subfolders, one for each assignment. Each of these subfolders contain the csv files with information about CO2 emissions for each assignment, which was obtained by implementing functions from [CodeCarbon](https://codecarbon.io/) in the source code in Assignments 1-4. 

- Csv files that ends with *'FULL_emissions.csv'* contain information about running the **entire** script
- Csv files that ends with *'subtasks_emissions.csv'* contain information about emissions for each **subtask** in a script
- Csv files that ends with *'subtasks_meta.csv'* contain metadata on emissions from subtasks, and are not used for this analysis directly.



As some of the assignments consists of running multiple scripts seperately, there will be several .csv files ending with *'FULL_emissions'* and *'subtasks_emissions'*. These csv files are concatenated in the ```src/visualize.py``` script to gather it into a full assignment.



### Usage

All code for this assignment was designed to run on an Ubuntu 24.04 operating system using Python version 3.12.2. It is therefore not guaranteed that it will work on other operating systems.

It is important that you run all code from the main folder, i.e., *assignment-5-evaluating-environmental-impact-louisebphansen*. Your terminal should look like this:

```
--your_path-- % assignment-5-evaluating-environmental-impact-louisebphansen %
```

#### Set up virtual environment

To run the code in this repo, clone it using ```git clone```.

In order to set up the virtual environment, the *venv* package for Python needs to be installed first:

```
sudo apt-get update

sudo apt-get install python3-venv
```

Next, run:

```
bash setup.sh
```

This will create a virtual environment in the directory (```env```) and install the required packages to run the code.

#### Run code

To run the code, you can do the following:

##### Run script with predefined arguments

To run the code in this repo with predefined/default arguments, run:
```
bash run.sh
```