# Importing required modules
from collections import Counter
import numpy as np
import warnings
import statistics
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# Exclude any future warnings (some decaprecated features used)
warnings.simplefilter(action="ignore", category=FutureWarning)
# Storage is the database used in the program
storage = {}

# The below prints the title
print("================================== Datation 2 ==================================")
print("The Python Calculator giving you calculations from your data, and making graphs.\n")
print("                                                                    - By Thinuka\n")


# yes_no is a simple yes and no prompt that takes in the question and makes a yes no prompt out of it
def yes_no(answer):
    # This defines what yes and no can be
    yes = {'yes', 'y', 'ye', ''}
    no = {'no', 'n'}

    # This makes a while loop for incase the person enters something other than what is in the defined list
    while True:
        # Makes the input lowercase
        choice = input(answer).lower()
        # The if statements below check if the person responded with yes or no, if not, it loops back to the prompt
        # If they did, yes returns true and no returns false
        if choice in yes:
            return True
        elif choice in no:
            return False
        else:
            print("Please respond with 'yes' or 'no'\n")


# isodd just checks if the the number is odd by running a calculation on it
def isodd(num):
    if (num % 2) == 0:
        return False
    else:
        return True


def calculate():
    # The global statements make these variables accessable from any other function
    global data_dataset
    global no_scores_dataset
    global mean_dataset
    global median_dataset
    global mode_dataset
    global range_dataset
    global low_median_dataset
    global high_median_dataset
    global variance_dataset
    # The function first does calculations from the array
    no_scores_dataset = len(data_dataset)
    mean_dataset = np.mean(data_dataset)
    median_dataset = np.median(data_dataset)
    mode_dataset = mode()
    range_dataset = np.ptp(data_dataset)
    variance_dataset = statistics.variance(data_dataset)
    # The if statement checks if the dataset has an odd number of values as low and high median only apply to them
    if isodd(len(data_dataset)):
        low_median_dataset = statistics.median_low(data_dataset)
        high_median_dataset = statistics.median_high(data_dataset)

    # Now it prints them
    print("\n\n============== Results of Calculations ==============")
    print(f"Number of Scores: {no_scores_dataset}")
    print(f"Mean: {mean_dataset}")
    print(f"Median: {median_dataset}")
    print(f"Mode: {mode_dataset}")
    print(f"Range: {range_dataset}")
    print(f"Variance: {variance_dataset}")
    if isodd(len(data_dataset)):
        print(f"Low Median: {low_median_dataset}")
        print(f"High Median: {high_median_dataset}")


# Dataset input is a function for inputting the dataset (numbers)
def dataset_input():
    # Global imports are to make the specified variables available to all functions and anything outside a function
    global name_dataset
    # It makes a while loop for the prompt to restart if the user inputs something other than a number
    while True:
        # Asks for user input
        user_input = input(f"Enter the data for dataset {name_dataset} (separated by spaces): ")
        # makes it a list
        lst = user_input.split()
        # It checks if everything the user entered is a number
        # If not, it restarts the prompt
        # If everything is a number, it makes it an array and returns it
        for i in lst:
            try:
                float(i)
                data = [float(item) for item in lst]
                data = np.array(data)
                return data
            except ValueError:
                print("Uh-oh! You seem to have entered a character other than a number. Please try again!\n")


# This function allows the user to access the database
def access_database():
    # It makes a while loop for the prompt to restart
    restart = True
    while restart:
        # Asks the user (using yes_no) if they would like to access the database
        access = yes_no("\nWould you like to access any of your saved datasets? (y/n) ")
        # If they say yes, it asks for the name of the dataset
        if access:
            dataset_name = input("Please enter the name of the dataset you want to access: ")
            # It gets that dataset and stores it in access_dataset
            access_dataset = storage.get(dataset_name)
            # It then checks if the dataset is valid to avoid errors
            if str(access_dataset) == 'None':
                print("Invalid dataset. Please try again.")
            else:
                # If it is, it prints it out
                for key, value in access_dataset.items():
                    print(key, ' : ', value)
        else:
            restart = False


# This function allows the user to save to the database
def save_database():
    # Global imports are to make the specified variables available to all functions and anything outside a function
    global name_dataset
    global data_dataset
    global storage
    # First it uses a yes_no prompt to ask the user if they want to save the dataset into the database
    save = yes_no("\nWould you like to save this data in a database? (y/n) ")
    if save:
        # If they do, it saves it under the name of the dataset in the database (a dictionary)
        # Its different depending on if there is a low median and high median or not.
        if isodd(len(data_dataset)):
            storage[name_dataset] = {
                'Data': data_dataset,
                'Number of Scores': no_scores_dataset,
                'Mean': mean_dataset,
                'Mode': mode_dataset,
                'Range': range_dataset,
                'Variance': variance_dataset,
                'Low Median': low_median_dataset,
                'High Median': high_median_dataset,
            }
        else:
            storage[name_dataset] = {
                'Data': data_dataset,
                'Number of Scores': no_scores_dataset,
                'Mean': mean_dataset,
                'Mode': mode_dataset,
                'Range': range_dataset,
                'Variance': variance_dataset,
            }


# This function gets the mode from a dataset
def mode():
    # Global imports are to make the specified variables available to all functions and anything outside a function
    global data_dataset
    # The line below runs the Counter function on our list. The Counter function makes the variable counter a
    # container that holds the count of each of the elements that are available in the container
    counter = Counter(data_dataset)
    # The code below finds the most common items in the list
    answer = [item for item, variable in counter.items() if variable == counter.most_common(1)[0][1]]
    # The if function below checks if all the numbers are most common (all entered the same amount of times),
    # and if they are, it returns "No Mode"
    if len(answer) == len(data_dataset):
        answer = "No Mode"
        return answer
    # Otherwise, it returns the modes that it found.
    else:
        return answer


# This function makes a graph out of how many times each number occured
def occurences_graph():
    # Global imports are to make the specified variables available to all functions and anything outside a function
    global data_dataset
    # It first uses a yes_no prompt to ask the user if they want to display the graph
    display = yes_no(
        f"\nWould you like to display a histogram on the occurences of each number in your dataset (y/n)? ")
    # If so, it makes the graph with matplotlib
    if display:
        # ax is defined as if it isnt defined, it will come up with some errors
        ax = plt.figure().gca()
        # This makes sure that all the ticks on the y axis are integers as you cannot have half an occurence
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))
        # It then makes a histogram with black borders
        plt.hist(data_dataset, ec="black")
        # The below makes labels and the title
        plt.xlabel('Number')
        plt.ylabel('Amount of occurences')
        plt.title('Histogram showing number of occurences')
        # It then shows it to the user
        plt.show()


# This function makes a line graph with the mean
def line_graph():
    # Global imports are to make the specified variables available to all functions and anything outside a function
    global mean_dataset
    global data_dataset
    # It first uses a yes_no prompt to ask the user if they want to display the graph
    display = yes_no(f"\nWould you like to display a line graph of your dataset with the mean (y/n)? ")
    # If so, it makes the graph with matplotlib
    if display:
        # plt.cla clears the previous graph incase of a collison
        plt.cla()
        # axhline makes a singular line going throught the middle representing the mean
        # The line will be red
        plt.axhline(y=mean_dataset, color='r', linestyle='-', label="Mean")
        # It then plots the line graph with the data from my dataset
        plt.plot(data_dataset)
        # The below makes labels and the title
        plt.title("Line graph displaying mean")
        plt.xlabel("Place in dataset")
        plt.ylabel("Value")
        # This makes a legend to indicate to the user that the red line is the mean
        plt.legend()
        # It then shows it to the user
        plt.show()


# This function uses a yes_no function to ask the user if they want to run the program again
def restart():
    restart = yes_no("\nWould you like to run this program again? (y/n) ")
    if not restart:
        print("Thank you for using the Datation Calculator. Please come back soon!")
    else:
        print("================================================================================")
        # If they do, it runs the function main (where all the code is)
        main()


# This function detects outliers
def detect_outliers(m=2):
    # Global imports are to make the specified variables available to all functions and anything outside a function
    global data_dataset
    # It runs the below calculation to determine any outliers and spits out an array that has them removed
    data_dataset_filtered = data_dataset[abs(data_dataset - np.mean(data_dataset)) < m * np.std(data_dataset)]
    # It then checks if the two arrays to see if they are the same
    if len(data_dataset_filtered) != len(data_dataset):
        # If so, it asks the user if the would like to remove it
        remove = yes_no(f"\nAn outlier was detected. \nThe currently entered dataset is:\n {data_dataset} \nand with "
                        f"the outlier removed, the dataset looks like this: \n {data_dataset_filtered}. \nWould you "
                        f"like to remove it? (y/n) ")
        if remove:
            # If they say they do, it changes the data_dataset variable (the variable storing numbers) to the one
            # without the outliers
            data_dataset = data_dataset_filtered


# I prefer to keep all my main code in a function named main to sort everything out.
# It is also useful to loop back to the beginning of the code
def main():
    # Global imports are to make the specified variables available to all functions and anything outside a function
    global storage
    global name_dataset
    # The below line of code asks the user if they want to enter the name of the dataset
    name_dataset = input("\nPlease enter the name of your dataset: ")
    global data_dataset
    # data_dataset becomes the return of dataset_input because the function returns the dataset
    data_dataset = dataset_input()

    # Calls the function to detect outliers
    detect_outliers()

    # Calls the function to run the calculations
    calculate()

    # Calls the function to ask the user if they want to save to the database
    save_database()

    # Calls the function to ask the user if they want to access the database
    access_database()

    # Calls the function to ask the user if they want a graph from the amount of times each number occured in the
    # dataset
    occurences_graph()

    # Calls the function to ask the user if they want a graph from their dataset and the mean
    line_graph()

    # Calls the function to ask the user if they want to restart the program
    restart()


# Calls the function main() to kickstart the program
main()
