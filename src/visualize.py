'''
LANGUAGE ANALYTICS @ AARHUS UNIVERSITY, ASSIGNMENT 5: Evaluating environmental impact

AUTHOR: Louise Brix Pilegaard Hansen

DESCRIPTION:
This script creates visualizations from .csv files in the input folder containing CO2 emissions for each assignment

'''

import os
import argparse
import pandas as pd 
import matplotlib.pyplot as plt 
import matplotlib.patches as mpatches

# define argument parser
def argument_parser():

    parser = argparse.ArgumentParser()

    parser.add_argument('--emissions_folder', type=str, help='name of emissions folder containing subfolders (with csv files) for each assignment', default = 'emissions')
    
    args = vars(parser.parse_args())
    
    return args

def total_emissions_and_time(assignment_folder:str) -> float:
    
    '''
    Function to loop through csv files in a folder to find the files containing
    data of emissions from running the entire script (i.e., has the 'FULL_emissions.csv' ending).
    As some folders will contain more than one file with this ending, these files will be concatenated in order
    to calculate the total CO2eq emitted from running the script as well as the duration of running it. 

    Arguments:
        - assignment_folder: name of assignment folder to iterate over

    Returns:
        - emission: total emissions from running an assignment
        - duration: total duration from running an assignment
    '''
    
    # create empty list
    files = []

    # loop over csv files in the assignment folder
    for csv_file in sorted(os.listdir(assignment_folder)):

        # get csv files that contain emissions from running entire script
        if csv_file.endswith('FULL_emissions.csv'):
            files.append(csv_file)
    
    # create empty dataframe
    full_df = pd.DataFrame()
    
    # read csv file(s) as dataframe, and in case there are more than one, concatenate them
    for file in files:
        df = pd.read_csv(os.path.join(assignment_folder, file))
        full_df = pd.concat([full_df, df])
    
    # sum the emissions and duration columns to get the total value to the assignment
    emission = full_df['emissions'].sum()
    duration = full_df['duration'].sum()
    
    return emission, duration

def calc_total_emissions(emissions_folder_name:str) -> list:

    '''
    Loops over each assignment subfolder and extracts information about total CO2eq emitted and durations from running the script
    from the relevant csv file(s)

    Arguments:
        - emissions_folder_name: Name of folder with subfolders that contain emission csv files.
    
    Returns:
        - emissions: List of total CO2eq emitted from running each assignment
        - durations: List with duration of each assignment

    '''

    # create path to emissions folder
    emissions_path = os.path.join(emissions_folder_name)

    # create empty lists
    emissions = []
    durations = []

    # loop over each assignment subfolder in the emissions folder
    for subfolder in sorted(os.listdir(emissions_path)):

        # load path to subfolder
        subfolder_path = os.path.join(emissions_path, subfolder)

        # find csv file with total emissions for that assignment and save emission and duration values
        emission, duration = total_emissions_and_time(subfolder_path)

        # append values to list
        emissions.append(emission)
        durations.append(duration)
    
    return emissions, durations

def create_total_plots(emissions:list, durations:list):

    '''
    Creates two plots; one which displays the emissions across assignments and one which display duration for each assignment.
    The plots are saved in the 'out' folder.

    Arguments:
        - emissions: List of total CO2eq emitted from running each assignment
        - durations: List with duration of each assignment

    Returns:
        None
    '''

    # create list of assignment names
    assignments = ['Assignment 1', 'Assignment 2', 'Assignment 3', 'Assignment 4']

    # plot emissions across assignments and save to out folder
    plt.plot()
    plt.bar(assignments, emissions, color = ['green', 'blue', 'red', 'orange'])
    plt.ylabel('Emissions of CO₂eq in kilograms')
    plt.title('Emissions of CO₂eq across assignments')
    plt.tight_layout()
    out_path = os.path.join('out', 'total_emissions.png')
    plt.savefig(out_path)

    # duration for each assignment and save to out folder
    plt.plot()
    plt.bar(assignments, durations, color = ['green', 'blue', 'red', 'orange'])
    plt.ylabel('Duration (in seconds)')
    plt.title('Duration of assignments')
    plt.tight_layout()
    out_path = os.path.join('out', 'total_durations.png')
    plt.savefig(out_path)

def create_subtasks_df(assignment_folder_path:str) -> pd.DataFrame:

    '''
    Create a pandas dataframe with all subtasks for an assignment by concatenating .csv files containing subtasks for each script.

    Arguments:
        - assignment_folder_path: path to assignment subfolder containing .csv files with subtasks
    
    Returns:
        - subtasks_df: pandas dataframe with all subtasks for an assignment
    
    '''
    
    # create empty list
    files = []

    # loop over each csv file in the folder to find subtasks csv file(s)
    for csv_file in sorted(os.listdir(assignment_folder_path)):
        if csv_file.endswith('subtasks_emissions.csv'):
            files.append(csv_file)
    
    # create empty dataframe
    subtasks_df = pd.DataFrame()
    
    # read the csv files as dataframe and concatenate them to get all subtasks for an assignment
    for file in files:
        df = pd.read_csv(os.path.join(assignment_folder_path, file))
        subtasks_df = pd.concat([subtasks_df, df])
    
    return subtasks_df

def create_subtasks_plot(subtasks_df:pd.DataFrame, assignment_number:int):

    '''
    Plot emissions for each subtask for an assignment.
    Plot is saved in the /out folder.

    Arguments:
        - subtasks_df: pandas dataframe with all subtasks for an assignment
        - assignment_number: What assignment the subtask_df is for
    
    Returns:
        None

    '''
    # get task names and emissions from subtask df
    task_names = list(subtasks_df['task_name'])
    emissions = list(subtasks_df['emissions'])

    # plot emissions for each subtask and save to out folder
    fig, ax = plt.subplots(figsize = (8,6))
    ax.barh(task_names, emissions)
    ax.set_xlabel('Emissions of CO₂eq in kilograms')
    ax.set_title(f'Emissions of CO₂eq for tasks in Assignment {assignment_number}')
    fig.tight_layout()
    out_path = os.path.join('out', f'subtasks_emissions_assignment_{assignment_number}.png')
    plt.savefig(out_path)

def create_gathered_subtasks_plot(all_subtasks:pd.DataFrame):

    '''
    Create a single plot to compare all subtasks across assignments.
    The plot is saved in the /out folder.

    Arguments:
        - all_subtasks: pandas dataframe containing all subtasks for all assignments
    
    Returns:
        None
    '''

    # create empty list
    colors = []

    # create list of colors to use, based on assignment number
    for i in range(len(all_subtasks)):

        if all_subtasks['assignment'].iloc[i] == 1:
            colors.append('green')
        
        elif all_subtasks['assignment'].iloc[i] == 2:
            colors.append('blue')
        
        elif all_subtasks['assignment'].iloc[i] == 3:
            colors.append('red')
        
        elif all_subtasks['assignment'].iloc[i] == 4:
            colors.append('orange')

    # create plot of all subtasks
    fig, ax = plt.subplots(figsize = (8,6))
    ax.barh(list(all_subtasks['task_name']), list(all_subtasks['emissions']), color = colors)
    ax.set_xlabel('Emissions of CO₂eq in kilograms')
    ax.set_title('Emissions of CO₂eq for tasks in all assignments')
    fig.tight_layout()

    # manually create legend to explain color
    handles = [mpatches.Patch(color='green', label='Assignment 1'),
                mpatches.Patch(color='blue', label='Assignment 2'),
                mpatches.Patch(color='red', label='Assignment 3'),
                mpatches.Patch(color='orange', label='Assignment 4')]

    fig.legend(handles=handles, bbox_to_anchor=(0.98,0.94))
    
    # save to out folder
    out_path = os.path.join('out', 'emissions_all_subtasks.png')
    plt.savefig(out_path)

def visualize_subtasks(emissions_folder_path:str):

    '''
    Creates a plot with emissions for each subtask for each assignment as well as a plot with emissions for all subtasks across assignments.
    The plots are saved in the /out folder.

    Arguments:
        - emissions_folder_path: Path to folder with subfolders that contain emission csv files

    Returns:
        None
    
    '''

    # create an empty dataframe to append all subtasks to
    all_subtasks = pd.DataFrame()

    # loop over each assignment folder in the emissionf folder
    for i, v in enumerate(sorted(os.listdir(emissions_folder_path))):

        # define path to assignment folder
        subfolder_path = os.path.join(emissions_folder_path, v)

        # create df with subtasks from csv files from assignment subfolder
        subtasks_df = create_subtasks_df(subfolder_path)

        # add assignment variable (for all_subtasks df)
        subtasks_df['assignment'] = i + 1

        # create and save a plot with emissions for all subtasks for assignment
        create_subtasks_plot(subtasks_df, i+1)

        # add df with subtasks for df with all subtasks across assignments
        all_subtasks = pd.concat([all_subtasks, subtasks_df])
    
    # create a plot with emissions for all subtasks across assignments
    create_gathered_subtasks_plot(all_subtasks)

def visualize_and_save(emissions_folder_name:str):
    '''

    Create all plots displaying total emissions for all assignments, emissions for each subtask for each assignment as well as emissions for all subtasks across assignments.
    All plots are saved in the /out folder.

    Arguments:
        - emissions_folder_name: Name of folder with subfolders that contain emission csv files
    
    Returns:
        None
    '''

    # define path to emissions folder containing subfolders for each assignment
    folder_path = os.path.join(emissions_folder_name)

    # save emissions and durations and create plots for total emissions from scripts
    emissions, durations = calc_total_emissions(folder_path)
    create_total_plots(emissions, durations)

    # create subtasks visualizations
    visualize_subtasks(folder_path)

def main():

    # parse arguments
    args = argument_parser()

    # create visualizations and save to /out folder
    visualize_and_save(args['emissions_folder'])

if __name__ == '__main__':
   main()


