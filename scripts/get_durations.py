import os
import csv
import sys

def get_lines(file_path):
    """Reads the contents of a file and returns a list of lines。"""
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines

def get_sentence_duration(file_path):
    """
    Calculate the total duration of a sentence in seconds.
    
    Args:
        file_path: Path to the duration CSV file.
        
    Returns:
        Total duration(int) in seconds.
    """
    lines = get_lines(file_path)
    total_duration = 0
    # Process the file from the second line for skipping the title line.
    for line in lines[1:]:
        # Get duration data from the csv.
        duration = line.split(';')[1]  # Split the csv by ;, and get data from the second column.
        duration = int(duration)
        total_duration += duration
        
    return total_duration / 1000    # Convert milliseconds to seconds.
        
    
def main():
    """
    Calculate the total duration of each sentence and match with corresponding surprisal values.

    Args:
        duration_folder (str): Path to folder containing duration CSV files
        surprisal_path (str): Path to CSV file containing surprisal data

    Input paths:
        - data/duration/: Contains sentence1.csv etc.
        - data/surprisal.csv: CSV file with "Sentence" and "Surprisal" columns

    Output:
        results/data.csv: File containing two columns:
            - "duration": Sentence duration in seconds
            - "surprisal": Average surprisal for the sentence

    Usage:
        $ python scripts/get_durations.py data/duration/ data/surprisal.csv

    """

    duration_folder = os.path.join("data", "duration")
    surprisal_path = os.path.join("data", "surprisal.csv")
    output_dir = "results"
    output_csv = os.path.join(output_dir, "data.csv")
    os.makedirs(output_dir, exist_ok=True)


    # Get surprisal data.
    surprisal_values = []
    with open(surprisal_path, 'r', encoding='utf-8') as csv_file:
        # Creat csv dictionary reader.
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            surprisal_value = float(row['Surprisal'])
            surprisal_values.append(surprisal_value)

    # Combine surprisal and duration data.
    data = []
    # Sort by sentence numbering order.
    file_list = sorted(os.listdir(duration_folder))
    
    # Process all files.
    for file in file_list:
        # Get sentence index from file name.
        if file.endswith('.csv'):
            file_path = os.path.join(duration_folder, file)
            sentence_index = int(file.replace("sentence", "").replace(".csv", "")) - 1

            # Get sentence data.
            sentence_duration = get_sentence_duration(file_path)
            sentence_surprisal = surprisal_values[sentence_index]
            
            # Save twp types of data into a two-demension list.
            # Each row is a sub-list representing the duration and surprisal of a sentence.
            # Each sublist contains two elements.
            data.append([sentence_duration, sentence_surprisal])

    with open(output_csv, "w", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            
            # Writerows accepts two-dimensional lists.
            # It treats each sub-list in a two-dimensional list as a row.
            # The elements of each sub-list are treated as column values of that row.
            writer.writerow(["duration", "surprisal"])
            writer.writerows(data) 

    print(f"\nProcessed {len(data)} sentences")
    print(f"Combined data saved to {output_csv}")

if __name__ == "__main__":
    main()
    