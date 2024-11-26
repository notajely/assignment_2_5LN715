import math
from nltk import sent_tokenize, word_tokenize
from collections import defaultdict
from math import log
import sys, time


def get_lines(file_path):
    """
    Takes a file path and returns the lines in the file as a list of strings.

    Args:
        file_path (str): The path to the file to be read.
    
    Returns:
        list
    """
    with open(file_path, 'r') as file:
        # Read lines in the file, store them in a list.
        lines = file.readlines()
        str_list = []
        
        for line in lines:
            # Remove line breaks, and add the processed lines in the list.
            str_list.append(line.strip())
            
    return str_list


def get_unigrams(sentences):
    """
    Calculate and return the frequency of each unigram in a list of sentences.


    Args:
        setences (str): The list of sentences to tokenize and count unigrams.
    
    Returns:
        dict: A dictionary with unigrams as keys and their frequencies as values.

    """
    unigram_freq = defaultdict(int)
    for sentence in sentences:
        # Add <s>, <e> helps model understand sentence structure and boundaries.
        tokens = ['<s>'] + word_tokenize(sentence) + ['<e>']
        for token in tokens:
            unigram_freq[token] += 1
    return  dict(unigram_freq)


def get_bigrams(sentences):
    bigram_freq = defaultdict(int)
    for sentence in sentences:
        tokens = ['<s>'] + word_tokenize(sentence) +['<e>']
        for i in range(len(tokens) - 1):
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
    surprisal = -math.log2(probability)
    return surprisal


def get_bigram_surprisal(unigram_freq, bigram_freq):
    """
    Calculate the surprisal values for bigrams based on unigram and bigram frequencies.

    Args:
        unigram_freq (dict): A dictionary with unigrams as keys and their frequencies as values.
        bigram_freq (dict): A dictionary with bigrams as keys and their frequencies as values.

    Returns:
        dict: A dictionary with bigrams as keys and their surprisal values as values.
    """
    bigram_surprisal = {}  # Initialize an empty dictionary to store bigram surprisal values
    
    for bigram in bigram_freq:  
        bigram_count = bigram_freq[bigram]  # Get the frequency of the current bigram
        
        first_word = bigram[0]  # Extract the first word of the bigram
        unigram_count = unigram_freq.get(first_word, 0)  # Get the frequency of the first word (unigram)
        
        # Apply Add-One Smoothing to avoid zero probabilities
        smoothed_bigram_count = bigram_count + 1
        smoothed_unigram_count = unigram_count + 1
        
        # Calculate the conditional probability P(w2|w1)
        conditional_probability = smoothed_bigram_count / smoothed_unigram_count
        
        # Calculate the surprisal value for the conditional probability
        surprisal = get_surprisal(conditional_probability)
        bigram_surprisal[bigram] = surprisal
    
    return bigram_surprisal