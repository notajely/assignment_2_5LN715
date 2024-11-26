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
        lines_list = file.readlines()
        for line in lines_list:
            # Remove line breaks, and add the processed lines in the list.
            lines_list.append(line.strip())
            
    return lines_list


def get_unigrams(sentences):
    """
    Calculate and return the frequency of each unigram in a list of sentences.

    Args:
        sentences (list[str]): The list of sentences to tokenize and count unigrams.
    
    Returns:
        dict: A dictionary where the keys are bigrams (tuples of two consecutive words) 
        and the values are the corresponding frequencies.
    """
    unigram_freq = defaultdict(int)
    
    for sentence in sentences:
        sentence = sentence.lower()
        tokens = word_tokenize(sentence)
        for word in tokens:
            unigram_freq[word] += 1
        
    return dict(unigram_freq)        


def get_bigrams(sentences):
    """
    Generate bigrams from sentences and count their frequencies.

    Args:
        sentences (list[str]): A list of sentences.
    Returns:
        dict: A dictionary with bigrams as keys and their frequencies as values.
    """
    bigram_freq = defaultdict(int)
    
    for sentence in sentences:
        
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
        bigram_surprisal[bigram] = get_surprisal(con_prob)
    
    return bigram_surprisal