import pandas as pd 
import os
import matplotlib.pyplot as plt 

def total_emissions_and_time(folder):
    
    files = []

    for csv_file in sorted(os.listdir(folder)):
        if csv_file.endswith('FULL_emissions.csv'):
            files.append(csv_file)
    
    full_df = pd.DataFrame()
    
    for file in files:
        df = pd.read_csv(os.path.join(folder, file))
        full_df = pd.concat([full_df, df])
    
    emissions = full_df['emissions'].sum()
    duration = full_df['duration'].sum()
    
    return emissions, duration

# CHANGE NAME !!!
def total_emissions(folder_name):

    emissions_path = os.path.join(folder_name)

    emissions = []
    durations = []

    for folder in sorted(os.listdir(emissions_path)):

        subfolder_path = os.path.join(emissions_path, folder)

        emission, duration = total_emissions_and_time(subfolder_path)

        emissions.append(emission)
        durations.append(duration)
    
    return emissions, durations

def plotting_total(emissions, durations):

    assignments = [f'Assignment {i +1}' for i in range(len(emissions))]

    plt.plot()
    plt.bar(assignments, emissions, color = ['green', 'blue', 'red', 'orange'])
    plt.ylabel('Emissions of CO₂eq in kilograms')
    plt.title('Emissions of CO₂eq across assignments')
    
    out_path = os.path.join('out', 'total_emissions.png')
    plt.savefig(out_path)

    plt.plot()
    plt.bar(assignments, durations, color = ['green', 'blue', 'red', 'orange'])
    plt.ylabel('Duration (in seconds)')
    plt.title('Duration of assignments')
    
    out_path = os.path.join('out', 'total_durations.png')
    plt.savefig(out_path)

def subtasks_emissions_and_time(folder):
    
    files = []

    for csv_file in sorted(os.listdir(folder)):
        if csv_file.endswith('subtasks_emissions.csv'):
            files.append(csv_file)
    
    subtasks_df = pd.DataFrame()
    
    for file in files:
        df = pd.read_csv(os.path.join(folder, file))
        subtasks_df = pd.concat([subtasks_df, df])
    
    return subtasks_df

def create_subtasks_plot(subtasks_df, assignment_number):

    names = list(subtasks_df['task_name'])
    emissions = list(subtasks_df['emissions'])

    # create plot
    fig, ax = plt.subplots(figsize = (8,4))
    ax.barh(names, emissions)
    ax.set_ylabel('Emissions of CO₂eq in kilograms')
    ax.set_title(f'Emissions of CO₂eq for tasks in Assignment {assignment_number}')
    
    out_path = os.path.join('out', f'subtasks_emissions_assignment_{assignment_number}.png')

    plt.savefig(out_path)

def visualize_subtasks(path):

    all_subtasks = pd.DataFrame()

    for i, v in enumerate(sorted(os.listdir(path))):

        subfolder_path = os.path.join(path, v)

        subtasks_df = subtasks_emissions_and_time(subfolder_path)
        subtasks_df['assignment'] = i + 1
        create_subtasks_plot(subtasks_df, i+1)
        all_subtasks = pd.concat([all_subtasks, subtasks_df])

    # create plot of all subtasks
    fig, ax = plt.subplots(figsize = (6,4))
    ax.barh(list(all_subtasks['task_name']), list(all_subtasks['emissions']))
    ax.set_ylabel('Emissions of CO₂eq in kilograms')
    ax.set_title('Emissions of CO₂eq for tasks in all assignments')
    
    out_path = os.path.join('out', 'emissions_all_subtasks.png')
    plt.savefig(out_path)

def save_data(folder_name):

    folder_path = os.path.join(folder_name)

    # create plots for total emissions from scripts
    emissions, durations = total_emissions(folder_path)
    plotting_total(emissions, durations)

    visualize_subtasks(folder_path)

def main():

    save_data('emissions')

if __name__ == '__main__':
   main()


