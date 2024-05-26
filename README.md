# Assignment 5: Evaluating environmental impact of my exam portfolio

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
- Csv files that ends with *'subtasks_emissions.csv'* contain information about emissions for **subtasks** in a script

Subtasks for each assignment was measured using the *'Explicit Object'* from CodeCarbon, which allowed me to track specific lines of code and therefore also specific subtasks. On the other hand, emissions from running the enitire script was measured using a *decorator* object from CodeCarbon, which was placed before the *main* function of each script, where the entire code analysis was run. This enabled me to get a metric for running the entire script (See CodeCarbon [docs](https://mlco2.github.io/codecarbon/examples.html#using-the-explicit-object) on more information about tracking options). All the code was run on one u1-standard-16 machine on UCloud.

As some of the assignments consists of running multiple scripts seperately, there will be several .csv files ending with *'FULL_emissions'* and *'subtasks_emissions'* for some assignments. These csv files are concatenated in the ```src/visualize.py``` script when calculating the total emissions for each assignment.

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

##### Define arguments yourself

Alternatively, the script(s) can be run with different arguments:

```
# activate the virtual environment

python3 src/visualize.py --emissions_folder <emissions_folder>
```

**Arguments:**
- **emissions_folder:** Name of emissions folder containing subfolders (with csv files) for each assignment. Default: 'emissions'

### Results & Discussion

The resulting plots can all be found in the ```out``` folder, but will be displayed below as well. The plots can be used to answer the following questions:

#### Which assignment generated the most emissions in terms of CO₂eq? Explain why this might be.


This plot (```out/total_emissions.png```) shows the CO2eq emissions from running all code from each of the assignments. It is very clear that Assignment 1 emits a lot more CO2eq than the rest of the assignments. Assignment 4 emits a bit more CO2eq than Assignment 2, whereas Assignment 3 emits very little compared to the rest of the Assignments. It is however important to note that the emissions for Assignment 3 is only for running a single query search, which is naturally much less computationally expensive than the other Assignments. This makes it very difficult to compare it to the other Assignments, as they are just too different.

Nonetheless, 



#### Which specific tasks generated the most emissions in terms of CO₂eq? Again, explain why this might be.


#### How robust do you think these results are and how/where might they be improved?

Doesn't take into account that for example training the huggingface emotion classifier was very computationally heavy.