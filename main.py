from collections import Counter
import numpy as np
import warnings
import statistics
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

warnings.simplefilter(action="ignore", category=FutureWarning)
storage = {}

# The below prints are just the title
print("================================== Datation 2 ==================================")
print("The Python Calculator giving you calculations from your data, and making graphs.\n")
print("                                                                    - By Thinuka\n")


def yes_no(answer):
    # This defines what yes and no can be
    yes = {'yes', 'y', 'ye', ''}
    no = {'no', 'n'}

    # This makes a while loop for incase the person enters something other than what is in the defined list
    while True:
        # Makes the input lowercase
        choice = input(answer).lower()
        # The if statements below check if the person responded with yes or no, if not, it loops back to the prompt
        if choice in yes:
            return True
        elif choice in no:
            return False
        else:
            print("Please respond with 'yes' or 'no'\n")


def isodd(num):
    if (num % 2) == 0:
        return False
    else:
        return True


def calculate():
    global data_dataset
    # The global statements make these variables accessable from any other function
    global no_scores_dataset
    global mean_dataset
    global median_dataset
    global mode_dataset
    global range_dataset
    global low_median_dataset
    global high_median_dataset
    global variance_dataset
    # The function first does calculations from array
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


def dataset_input():
    global name_dataset
    while True:
        user_input = input(f"Enter the data for dataset {name_dataset} (separated by spaces): ")
        lst = user_input.split()
        for i in lst:
            try:
                float(i)
                data = [float(item) for item in lst]
                data = np.array(data)
                return data
            except ValueError:
                print("Uh-oh! You seem to have entered a character other than a number. Please try again!\n")


def access_database():
    restart = True
    while restart:
        access = yes_no("\nWould you like to access any of your saved datasets? (y/n) ")
        if access:
            dataset_name = input("Please enter the name of the dataset you want to access: ")
            access_dataset = storage.get(dataset_name)
            if str(access_dataset) == 'None':
                print("Invalid dataset. Please try again.")
            else:
                for key, value in access_dataset.items():
                    print(key, ' : ', value)
        else:
            restart = False


def save_database():
    global name_dataset
    global data_dataset
    global storage
    save = yes_no("\nWould you like to save this data in a database? (y/n) ")
    if save:
        if isodd(len(data_dataset)):
            storage[name_dataset] = {
                'Data': data_dataset,
                'Number of Scores': no_scores_dataset,
                'Mean': mean_dataset,
                'Mode': mode_dataset,
                'Range': range_dataset,
                'Variance': {variance_dataset},
                'Low Median': {low_median_dataset},
                'High Median': {high_median_dataset},
            }
        else:
            storage[name_dataset] = {
                'Data': data_dataset,
                'Number of Scores': no_scores_dataset,
                'Mean': mean_dataset,
                'Mode': mode_dataset,
                'Range': range_dataset,
                'Variance': {variance_dataset},
            }


def mode():
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


def occurences_graph():
    global data_dataset
    display = yes_no(
        f"\nWould you like to display a histogram on the occurences of each number in your dataset (y/n)? ")
    if display:
        ax = plt.figure().gca()
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))
        plt.hist(data_dataset, ec="black")
        plt.xlabel('Number')
        plt.ylabel('Amount of occurences')
        plt.title('Histogram showing number of occurences')
        plt.show()


def line_graph():
    global mean_dataset
    global data_dataset
    display = yes_no(f"\nWould you like to display a line graph with the mean (y/n)? ")
    if display:
        plt.cla()

        # Plot
        plt.axhline(y=mean_dataset, color='r', linestyle='-', label="Mean")
        plt.plot(data_dataset)

        plt.title("Line graph displaying mean")
        plt.xlabel("Place in dataset")
        plt.ylabel("Value")
        plt.legend()

        plt.show()


def restart():
    restart = yes_no("\nWould you like to run this program again? (y/n) ")
    if not restart:
        print("Thank you for using the Datation Calculator. Please come back soon!")
    else:
        print("================================================================================")
        main()


def detect_outliers(m=2):
    global data_dataset
    data_dataset_filtered = data_dataset[abs(data_dataset - np.mean(data_dataset)) < m * np.std(data_dataset)]
    if len(data_dataset_filtered) != len(data_dataset):
        remove = yes_no(f"\nAn outlier was detected. \nThe currently entered dataset is:\n {data_dataset} \nand with "
                        f"the outlier removed, the dataset looks like this: \n {data_dataset_filtered}. \nWould you "
                        f"like to remove it? (y/n) ")
        if remove:
            data_dataset = data_dataset_filtered


# I prefer to keep all my main code in a function named main to sort everything out.
def main():
    global storage
    global name_dataset
    name_dataset = input("\nPlease enter the name of your dataset: ")
    global data_dataset
    data_dataset = dataset_input()

    detect_outliers()

    calculate()

    save_database()

    access_database()

    occurences_graph()

    line_graph()

    restart()


main()
