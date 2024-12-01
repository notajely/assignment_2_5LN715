import pandas as pd
import matplotlib.pyplot as plt
import os

def create_histogram():
    """
    Create a histogram of the durations.

    Reads the 'data.csv' file, rounds the 'duration' values, and creates a histogram.
    The x-axis represents the durations, and the y-axis represents their frequencies.
    The histogram is saved as 'duration_histogram.png'.
    """
    # Prepare input and outputpath
    output_dir = "results"
    os.makedirs(output_dir, exist_ok=True)
    input_path = os.path.join(output_dir, "data.csv")
    output_path = os.path.join(output_dir, "duration_histogram.png")

    # Load the data from 'data.csv'
    data = pd.read_csv('results/data.csv')

    # Round the 'duration' column for histogram binning
    rounded_durations = data['duration'].round()

    # Create the histogram
    plt.hist(rounded_durations, bins=10, color='blue', edgecolor='black', alpha=0.7)

    # Add labels and title
    plt.xlabel('Duration (s)')  # Label for x-axis
    plt.ylabel('Frequency')    # Label for y-axis
    plt.title('Histogram of Rounded Durations')  # Title of the plot

    # Save the histogram as a PNG file
    plt.savefig('duration_histogram.png')
    plt.close()

    print("Histogram saved as 'duration_histogram.png'")

if __name__ == "__main__":
    create_histogram()
