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


This plot (```out/total_emissions.png```) shows the CO2eq emissions from running all code from each of the assignments. It is very clear that Assignment 1 emits a lot more CO2eq than the rest of the assignments. Assignment 4 emits a bit more CO2eq than Assignment 2, whereas Assignment 3 emits very little compared to the rest of the Assignments. It is however important to note that the emissions for Assignment 3 is only for running a single query search, which is naturally much less computationally expensive than the other assignments, as it is a much smaller task. This makes it very difficult to compare it to the other assignments, as they are just too different. With this in mind, it is nonetheless still possible to conclude that Assignment 1 omits the most CO2eq. Although it is arguably one of the most *simple* assignments in terms of NLP methods, it is apparently also the most computationally heavy. This is probably because several ```spaCy``` functions needs to be used on *all* documents in *all* subfolders. Each text in each subfolder needs to be tokenized, which uses some compute power. Furthermore, the code only looks for one POS or NER tag *at a time* - this means that the code goes through all words in each .txt file for every POS or NER tags to be counted, making it quite inefficient, because it has to go through a lot of text multiple times.

Next, Assignment 4 emits more CO2eq compared to Assignment 2. This is probably due to multiple things; first of all, the data for Assignment 4 (22,300 lines) is substatially bigger than the data for Assignment 2 (6335 texts). Second, the emotion classifier in Assignment 4 uses sentece transformers to create embeddings for the spoken lines, whereas Assignment 2 uses a more simple, TF-IDF vectorizer as input to the classifier. Furthermore, the classification head attatched to the pre-trained HuggingFace model used is arguably way more complex than the neural network or logistic regression model used in Assignment 2. However, considering these points, it is interesting that Assignment 4 does not emit even more CO2eq compared to Assignment 2. This arguably highlights the benefits of using pre-trained models compared to models trained from scratch.



Assignment 4 also requires some computational power. 

This makes sense as it applies a pre-trained emotion-classification transformer models to all 22,300 rows in the dataset. Even though 


#### Which specific tasks generated the most emissions in terms of CO₂eq? Again, explain why this might be.

##### Assignment 1

##### Assignment 2

The plot (```out/subtasks_emissions_assignment_2.png```) shows emissions for subtasks in Assignment 2. This clearly shows that fitting the neural network classifier emits the most CO2eq compared to the other tasks. Although it is a quite simple neural network, with only one hidden layer of size 50, training it from scratch is computationally expensive, as all the weights needs to be updated during fitting on the training data. On the other hand, the logistic regression does not have this hidden layer with weights to be updated, which explains the low CO2eq emitted from this model. It should be noted that the emissions for fitting the logistic model is of course not zero, but it is just so close to 0 that it becomes insignificant in the barplot.

These results are especially interesting considering the results from the classification task of Assignment 2, as the two models performed almost identically. This underlines that for a simple classification problem such as this, more complex models might not be the answer, especially considering the increase in CO2eq emissions compared to a simple, logistic regression.


##### Assignment 3

For Assignment 3, we see that loading the GLOVE embedding model is the most computationally heavy task. This is because the GLOVE model contains all the pre-trained word embeddings from the corpus (*wiki-gigaword-50*), making it a big file to load. On the other hand, the two other subtasks just process the data in simples ways, i.e., simple pre-processing where punctuation is removed and everything is made lowercase, as well as the query search, which is really just a word-counting task. Neither of these tasks are computationally expensive, even though they are applied to all songs in the dataset, which is why they do no emit a lot of CO2eq.

##### Assignment 4


#### How robust do you think these results are and how/where might they be improved?

Doesn't take into account that for example training the huggingface emotion classifier was very computationally heavy.