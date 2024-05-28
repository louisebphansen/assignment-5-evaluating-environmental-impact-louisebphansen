# Assignment 5: Evaluating the environmental impact of my exam portfolio

This assignment is the fifth and final assignment for the portfolio exam in the Language Analytics course at Aarhus University, spring 2024.

### Contributions

The code was written by me, but code provided in the notebooks for the course has been reused. 

### Assignment description

For this assignment, I want you to go back to all four of previous assignments in Language Analytics. For each assignment, I want you to use CodeCarbon to measure the environmental impact of your code in terms of CO₂eq. You should specifically address the following questions:

- Which assignment generated the most emissions in terms of CO₂eq? Explain why this might be.
- Which specific tasks generated the most emissions in terms of CO₂eq? Again, explain why this might be.
- How robust do you think these results are and how/where might they be improved?

### Contents of the repository

| <div style="width:120px"></div>| Description |
|---------|:-----------|
| ```out``` | Contains the output plots showing emissions for assignments and subtasks|
| ```src```  | Contains the Python script for generating plots of emissions |
| ```run.sh```    | Bash script for running Python script with default arguments|
| ```setup.sh```  | Bash script for setting up virtual environment|
| ```requirements.txt```  | Packages required to run the code|
|```emissions.zip```| Zipped datafolder containing all csv files with information about emissions from running code from Assignments 1-4|

### Methods & Data
This repository contains the code to visualize results from csv files containing information about CO2-equivalent emissions from running the code in Assignments 1-4. The csv files can be found in the ```emissions.zip``` file; unzipping it will create the folder ```emissions``` with four subfolders, one for each assignment. Each of these subfolders contain the csv files with information about CO₂eq emissions for each assignment, which was obtained by implementing functions from [CodeCarbon](https://codecarbon.io/) in the source code in Assignments 1-4. 

- Csv files that ends with *'FULL_emissions.csv'* contain information about running the **entire** script
- Csv files that ends with *'subtasks_emissions.csv'* contain information about emissions for **subtasks** in a script

Subtasks for each assignment was measured using the *'Explicit Object'* from CodeCarbon, which allowed me to track specific lines of code and therefore also specific subtasks. On the other hand, emissions from running the enitire script was measured using a *decorator* object from CodeCarbon, which was placed before the *main* function of each script, where the entire code analysis was run. This enabled me to get a metric for running the entire script (See CodeCarbon [docs](https://mlco2.github.io/codecarbon/examples.html#using-the-explicit-object) on more information about tracking options). As some of the assignments consists of running multiple scripts seperately, there will be several .csv files ending with *'FULL_emissions'* and *'subtasks_emissions'* for some assignments. These are concatenated in the script before calculating the full emissions for assignments, to get a single metric for each assignment. The emissions in the csv files are the result of running all code from Assignments 1-4 on one u1-standard-16 machine on UCloud.


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

This will unzip the ```emissions.zip``` file, creating the folder ```emissions```. Next, it runs the ```src/visualize.py``` script with default arguments. The resulting plots can be found in the ```out``` folder.

##### Define arguments yourself

Alternatively, the script can be run with different arguments:

```
# activate the virtual environment
source ./env/bin/activate

# unzip datafile 
unzip emissions.zip

# run script
python3 src/visualize.py --emissions_folder <emissions_folder>
```

**Arguments:**
- **emissions_folder:** Name of emissions folder containing subfolders (with csv files) for each assignment. Default: 'emissions'

### Results & Discussion

The resulting plots can all be found in the ```out``` folder, but will be displayed below as well. It is important to note that the tasks with no bar appearing from them do not have a CO₂eq emission of zero, they are just so small and close to zero that they do not appear on the plot.

The plots can be used to answer the following questions:

#### Which assignment generated the most emissions in terms of CO₂eq? Explain why this might be.

![image](https://github.com/louisebphansen/assignment-5-evaluating-environmental-impact-louisebphansen/assets/75262659/2bd67d06-0470-4262-b36e-0676370ed71a)

This plot (```out/total_emissions.png```) shows the CO₂eq emissions from running all code in each of the assignments. It is very clear that Assignment 1 emits a lot more CO₂eq than the rest of the assignments. Assignment 4 emits a bit more CO₂eq than Assignment 2, whereas Assignment 3 emits very little compared to the rest of the Assignments. It is however important to note that the emissions for Assignment 3 is only for running a *single* query search, which is naturally much less computationally expensive than the other assignments, as it is a much smaller task. This makes it very difficult to compare it to the other assignments, as they are too different in size. With this in mind, it is nonetheless still possible to conclude that Assignment 1 omits the most CO₂eq. Although it is arguably one of the most *simple* assignments in terms of NLP methods, it is apparently also the most computationally heavy. This is probably because several ```spaCy``` functions needs to be used on *all* text files in *all* subfolders. First, each text in each subfolder needs to be tokenized, which uses some compute power. Furthermore, the code only looks for one POS or NER tag *at a time* - this means that the code goes through all words in each .txt file for every POS or NER tags to be counted, making it quite inefficient, because it has to go through a lot of text multiple times.

Furthermore, one can conclude from the plot that Assignment 4 emits more CO₂eq compared to Assignment 2. There could be several reasons for this. First of all, the data for Assignment 4 (22,300 lines) is substatially bigger than the data for Assignment 2 (6335 texts). Second, the emotion classifier in Assignment 4 uses a more complex and computationally heavy pre-trained sentence transformer to create embeddings for the spoken lines, whereas Assignment 2 uses a more simple, TF-IDF vectorizer as input to the classifier. However, considering this, it is interesting that Assignment 4 does not emit even more CO₂eq compared to Assignment 2. This arguably highlights the benefits of using pre-trained models compared to models trained from scratch, as it saves you a lot of computational ressources. 

#### Which specific tasks generated the most emissions in terms of CO₂eq? Again, explain why this might be.

The following plots shows the emissions for subtasks in each Assignment.

##### Assignment 1

![image](https://github.com/louisebphansen/assignment-5-evaluating-environmental-impact-louisebphansen/assets/75262659/b366fd43-ab23-4609-bb5c-abd7c98cee4e)

The plot for subtasks in Assignment 1 very evidently displays that extracting linguistic features emits more CO₂eq compared to downloading the ```spaCy``` model. The reasons for this are described in more detail in the section above, but is probably due to the fact that going through all texts in all subfolders and applying ```spaCy``` methods is a quite computationally heavy task. However, one could argue that it would have been more informative to track emissions from tasks *within* the *extracting linguistic information* task, in order to see whether it for example took more compute power to find POS tags than NER instances. The way the code was structured did not allow for this, but it should definitely be considered for future reference. 

##### Assignment 2

![image](https://github.com/louisebphansen/assignment-5-evaluating-environmental-impact-louisebphansen/assets/75262659/108bbe02-5e4a-411c-94dc-4fd08d0f28b7)

This plot clearly shows that fitting the neural network classifier emits the most CO₂eq compared to the other tasks. Although it is a quite simple neural network, with only one hidden layer of size 50, training it from scratch is computationally expensive, as all the weights needs to be updated during training. On the other hand, logistic regression models are more simple with fewer parameters and are therefore easier to implement. These results are especially interesting considering the results from the classification task of Assignment 2, as the two models performed almost identically. This underlines that for a simple classification problem such as this, more complex models might not be the answer, especially considering the increase in CO₂eq emissions compared to a simple, logistic regression. Finally, we can see that although vectorizing the data does not emit as much CO₂eq as fitting the neural network, it still requires some computational ressources. Therefore, it seems to be a good idea, which is also done for Assignment 2, to vectorize the dataset *once* and save it, instead of doing it twice when fitting the logisitc regression and neural network seperately, as it saves some computational ressources.


##### Assignment 3

![image](https://github.com/louisebphansen/assignment-5-evaluating-environmental-impact-louisebphansen/assets/75262659/211839b9-9bed-41ee-aaff-52694fe1ba80)

For Assignment 3, we see that loading the GloVe embedding model is the most computationally heavy task. This is because the GloVe model contains all the static, pre-trained word embeddings from the corpus (*wiki-gigaword-50*), making it a big file to load. On the other hand, the two other subtasks just process the data in simple ways, i.e., simple pre-processing where punctuation is removed and everything is made lowercase, as well as the query search, which is really just a word-counting task. Neither of these tasks are computationally expensive, even though they are applied to all songs in the dataset, which is why they do no emit a lot of CO₂eq. However, it should again be noted that the emissions displayed here is only for a *single* query search. One could for example imagine that the plot would look different if the task was to search for a long list of search terms with each run, which would make the query search task more computationally expensive. 

##### Assignment 4

![image](https://github.com/louisebphansen/assignment-5-evaluating-environmental-impact-louisebphansen/assets/75262659/cbe4c037-b7d4-485b-b021-f5860cd05438)

For this assignment, it is evident that using the pre-trained emotion classifier to predict emotion labels for all lines in the data was the task that emitted the most CO₂eq. We see that loading and initializing the HuggingFace classification pipeline does not appear to be very computationally expensive, for example compared to loading the GloVe model of Assignment 3. One could imagine that HuggingFace, an organization specialized in hosting state-of-the-art pre-trained models for many different applications, have optimized their model storage and loading in a way that it does not require too much compute power to load it, making it more efficient for the user to employ. On the other hand, classifying emotions appears to be quite computationally expensive, which makes sense, as all 22,300 lines in the data has to be processed by the pre-trained model in order to predict emotion labels. Even though it is a pre-trained model and does not need to be trained from scratch, it first needs to extract sentence-embeddings from the text before making predicitions, which requires a lot of compute power. 


##### All assignments

![image](https://github.com/louisebphansen/assignment-5-evaluating-environmental-impact-louisebphansen/assets/75262659/42ffca29-c03e-4dae-a457-23a77c23f4ea)

In this plot, all subtasks for all assignments are gathered into a single plot. We see the same trends as described in the sections above; extracting linguistic information from Assignment 1 is the task which emits the most CO₂eq, followed by classifying emotions in Assignment 4 and fitting a neural network in Assignment 2. It is evident that 'simple' tasks, such as plotting results, pre-processing text or fitting a logistic regression emits very little CO₂eq, as they require a much more simple processing of the data. On the other hand, tasks such as extracting linguistic information, classifying emotions or fitting a model from scratch, emits a lot more CO₂eq, as they require much more complex and computationally expensive processing of data.

#### How robust do you think these results are and how/where might they be improved?


The results are robust in the way that running the code again on the same UCloud machine would give the same results. There are, however, arguably some limitations in the way CodeCarbon measures emissions.

![image](https://github.com/louisebphansen/assignment-5-evaluating-environmental-impact-louisebphansen/assets/75262659/b848c4f0-9005-4e85-924c-c175f7f6acdc)

This plot shows the duration from running each assignment on the u1-standard-16 machine on UCloud. One might notice that the heights of the barplots looks identical to the ones in the plot of emissions across assignments, which indicates that the most important factor which determines how much CO₂eq a script of code emits is the time it takes running it. CodeCarbon notes in their [documentation](https://mlco2.github.io/codecarbon/methodology.html) that the CO₂eq emissions are measured using the following formula:

```C * E```

Where C is the "*carbon intensity of the electricity consumed*" and E is the "*kilowatt-hours*". This means that CodeCarbon uses a constant, *C*, to multiply with time spent running the code, *E*. This *C* variable seems to be determined by how energy is produced in the country the code is run from. A country with energy sources mainly from wind power would for example have a lower carbon intensity than a country that uses mainly coal as an energy source (again, see CodeCarbon [docs](https://mlco2.github.io/codecarbon/methodology.html) for more information). This could mean that running the code in a country with energy sources different from Denmark's would give different results in terms of CO₂eq emissions, which does not make the results robust across locations or nations. Although one could argue that CodeCarbon has come up with a fairly decent and simple measure of estimating CO₂eq emissions, it is not entirely clear how precise or updated the numbers used for these calculations are, which introduces a lot of uncertainty. One could therefore argue that the numbers from CodeCarbon should not be interpreted as the ground truth, but rather a way to estimate emissions or compare emissions across tasks to be mindful of the impact your code might have.

Furthermore, CodeCarbon does not appear (from their formula, at least) to take into account what type of machine the code is run on. This could for example become a problem on a computing service such as UCloud, where it is possible to select what size of machine you want your code to run on, and where bigger machines often result in faster compute time. One could have the assumption that bigger machines, even though they run the code faster, also emits more CO₂ when used. If this is the case, CodeCarbon overlooks this source of emissions, which again makes their metrics imprecise. It would thus be beneficial if there was a way for CodeCarbon to include this in their measurements of CO₂eq, and even better if there was of ensuring that one were using the optimal resources (in terms of compute power) for the task at hand. This could ensure a fair trade-off between efficient use of compute power to reduce CO₂ emissions and speed. 
