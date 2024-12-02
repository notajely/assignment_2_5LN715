import math
from nltk import sent_tokenize, word_tokenize
from collections import defaultdict
from math import log
import sys, time
import re
import os
import csv


def get_lines(train_path):
    """
    Takes a file path and returns the train_sentences in the file as a list of strings.

    Args:
        train_path (str): The path to the file to be read.
    
    Returns:
        list: A list of filtered train_sentences.
    """
    with open(train_path, 'r', encoding='utf-8') as file:
        text = file.read()
        
    train_sentences = sent_tokenize(text)  # Tokenize text into train_sentences
    return [sentence.strip() for sentence in train_sentences if sentence.strip()]


def get_unigrams(train_sentences):
    """
    Calculate and return the frequency of each unigram in a list of train_sentences.

    Args:
        train_sentences (list[str]): The list of train_sentences to tokenize and count unigrams.
    
    Returns:
        dict: A dictionary where the keys are unigrams (single words) 
              and the values are their corresponding frequencies.
    """
    unigram_freq = defaultdict(int)
    
    for sentence in train_sentences:
        sentence = sentence.lower() 
        tokens = word_tokenize(sentence)
        for word in tokens:
            unigram_freq[word] += 1
            
    return dict(unigram_freq)
        


def get_bigrams(train_sentences):
    """
    Generate bigrams from train_sentences and count their frequencies.

    Args:
        train_sentences (list[str]): A list of train_sentences.
    
    Returns:
        dict: A dictionary where the keys are bigrams (tuples of two consecutive words) 
              and the values are their corresponding frequencies.
    """
    bigram_freq = defaultdict(int)
    
    for sentence in train_sentences:
        
        sentence = sentence.lower()
        tokens = word_tokenize(sentence)
        
        # Iterate through the list of words after tokeniaztion and generate all neighboring word pairs 
        for i in range(len(tokens) - 1):
            # When tokens[i] and tokens[i + 1] appear together, update bigram count.
            bigram = (tokens[i], tokens[i + 1]) # bigram = (w1,w2)
            bigram_freq[bigram] += 1    # bigram_freq = {(w1, w2): 1}
            
    return dict(bigram_freq)


def get_surprisal(probability):
    """
    Calculate the surprisal value for a given probability.

    Args:
        probability (float): The probability value.

    Returns:
        float: The surprisal value.
    """
    # Make sure the probability in range of (0, 1).
    if probability <= 0 or probability > 1:
        raise ValueError("Invalid probability value.")
    
    surprisal = -math.log2(probability)
    
    return surprisal


def get_bigram_surprisal(unigram_freq, bigram_freq):
    """
    Calculate the surprisal values for bigrams based on unigram and bigram frequencies.

    Args:
        unigram_freq (dict): A dictionary with unigrams as keys and their frequencies as values.
        bigram_freq (dict): A dictionary where the keys are bigrams (tuples of two consecutive words) 
        and the values are the corresponding frequencies.

    Returns:
        dict: A dictionary with bigrams as keys and their surprisal values as values.
    """
    # Initialize an empty dictionary to store bigram surprisal values.
    bigram_surprisal = {}  
    
    for bigram in bigram_freq:  
        
        # Get the frequency of the bigram.
        bigram_count = bigram_freq[bigram] 
        
        # Extract the first word of the bigram.
        first_word = bigram[0]
        # Get the frequency of the first word.
        unigram_count = unigram_freq.get(first_word, 0)
        
        # Apply Add-One Smoothing to avoid zero probabilities
        smoothed_bigram_count = bigram_count + 1
        smoothed_unigram_count = unigram_count + 1
        
        # Calculate the conditional probability P(w2|w1)
        con_prob = smoothed_bigram_count / smoothed_unigram_count
        
        # Calculate the surprisal value for the conditional probability
        surprisal = get_surprisal(con_prob)
        bigram_surprisal[bigram] = surprisal
    
    return bigram_surprisal


def get_test_surprisal(sentence, bigram_surprisal, default_surprisal=10):
    """
    Calculates the average surprisal value for a given sentence based on a precomputed bigram surprisal dictionary.

    Args:
        sentence (str): The input sentence for which surprisal needs to be calculated.
        bigram_surprisal (dict): A dictionary with bigrams as keys and their surprisal values as values.
        default_surprisal (float): The default surprisal value to use if a bigram is not found in the dictionary.

    Returns:
        float: The average surprisal value for the sentence. Returns None if there are no bigrams in the sentence.
    """
    # Convert the sentence to lowercase and tokenize it into words.
    sentence = sentence.lower()
    tokens = word_tokenize(sentence)

    # Initialize counters for total surprisal and the number of bigrams.
    total_surprisal = 0
    bigram_count = 0

    # Iterate through the tokens to generate bigrams and calculate surprisal.
    for i in range(len(tokens) - 1):
        bigram = (tokens[i], tokens[i + 1])  # Form a bigram from two consecutive tokens.
        surprisal = bigram_surprisal.get(bigram, default_surprisal)  # Get surprisal or use default.
        total_surprisal += surprisal  # Add the surprisal to the total.
        bigram_count += 1  # Increment the bigram count.

    # Return the average surprisal if there are bigrams, otherwise return None.
    if bigram_count > 0:
        return total_surprisal / bigram_count
    else:
        return None



def main():
    """
    Calculate surprisal values for test sentences using a trained bigram model.
    
    1. Trains a bigram language model using training data
    2. Selects 10 eligible sentences from test data
    3. Calculates surprisal values for selected sentences
    4. Saves results:
       - Individual text files for each sentence
       - CSV file with sentence-surprisal pairs

    Args:
        train_path (sys.argv[1]): Path to training corpus file
        test_path (sys.argv[2]): Path to test corpus file

    Outputs:
        - data/10_sentences/: Directory containing text files for each valid sentence
        - data/surprisal.csv: CSV file with columns "Sentence" and "Surprisal"

    Usage:
        $ python scripts/get_surprisals.py data/external/wiki.train.raw data/external/wiki.test.raw
    
    Note:
        Sentences are valid if they:
        - Don't contain special characters
        - Aren't title lines
        - Have at least 15 tokens
        - Contain all bigrams from bigram dictionary
    """
    
    train_path = sys.argv[1]
    test_path = sys.argv[2]
    # Prepare data-saving path.
    base_dir = "data"
    sentences_dir = os.path.join(base_dir, "10_sentences")
    output_csv = os.path.join(base_dir, "surprisal.csv") 
    os.makedirs(sentences_dir, exist_ok=True)

    # 1.Train bigram model.
    train_sentences = get_lines(train_path)
    unigram_freq = get_unigrams(train_sentences)
    bigram_freq = get_bigrams(train_sentences)
    bigram_surprisal = get_bigram_surprisal(unigram_freq, bigram_freq)
    
    # 2.Select 10 eligible sentences
    test_sentences = get_lines(test_path)
    valid_sentence = []
    
    # Regular expressions are used to find special charaters, and title lines.
    special_pattern = re.compile(r"[^\w\s,.]")
    title_pattern = re.compile(r"^\s*=+\s+.*\s+=+\s*$")
    
    with open(output_csv, "w", newline="", encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Sentence", "Surprisal"])  

        for sentence in test_sentences:
            sentence = special_pattern.sub("", sentence).strip()    # Remove special characters and blank space from two ends.
            
            # Skip title lines.
            if title_pattern.match(sentence):
                continue
            
            # Basic preprocessed.
            sentence = sentence.lower()
            tokens = word_tokenize(sentence)
            if len(tokens) < 15:
                continue
            
            # Use bool to track if the sentence is eligible.
            valid = True
            
            for i in range(len(tokens) - 1):
                bigram = (tokens[i], tokens[i + 1])
                
                # Skip sentences with any bigram is not in bigram ditionary.
                if bigram not in bigram_freq:
                    valid = False
                    break
            
            if valid:
                # 3.Calculates surprisal values for selected sentences
                avg_surprisal = get_test_surprisal(sentence, bigram_surprisal)
                
                # Add valid sentence into the list.
                valid_sentence.append(sentence)

                # 4.Save results
                output_path = os.path.join(sentences_dir, f"sentence{len(valid_sentence)}.txt")
                
                with open(output_path, "w", encoding="utf-8") as file:
                    file.write(sentence)
                    
                # Save sentence and its surprisal into csv.
                csv_writer.writerow([sentence, avg_surprisal]) 
                
                # Continue until find 10 valid sentences.
                if len(valid_sentence) == 10: 
                    break
    
    # Preventing program execution from continuing without a valid sentence。
    if valid_sentence:
        print("Get all surprisal of test sentences")
    else:
        print("No valid sentences found.")

if __name__ == "__main__":
    main()
    