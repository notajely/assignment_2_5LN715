# **Assignment 2 - Advanced Programming (5LN715)**

## **Project Overview**

This project is the second assignment for the **Advanced Programming (5LN715)** course at Uppsala University. It aims to study the relationship between speech clarity and information content (Surprisal) by analyzing speech duration and linguistic information content, verifying the hypothesis that speech clarity is positively correlated with information content.

## **Objectives**

1. **Data Processing**:
* Train a bigram model using `wiki.train.raw` data.
* Extract information content from `wiki.test.raw` data and generate sentence Surprisal values.
2. **Speech Data Collection**:
* Record speech data corresponding to the test sentences.
* Use **MAUS (Munich Automatic Segmentation System)** to extract phoneme durations.
* Use **ffmpeg** to convert audio format.
3. **Analysis and Modeling**:
* Use a linear regression model to explore the relationship between speech clarity (duration) and information content (Surprisal).
* Visualize data using histograms and regression plots.

## **File Structure**

The project file structure is as follows:

```plaintext
assignment_2_5LN715/
│
├── data/                           # Data directory
│   ├── external/                   # Raw data: wiki.train.raw, wiki.test.raw
│   ├── 10_sentences/               # Selected 10 sentences
│   ├── duration/                   # Duration data obtained from MAUS
│   ├── surprisal.csv               # Surprisal data of each sentence
│
├── scripts/                        # Core Python scripts
│   ├── get_durations.py            # Extract speech durations from MAUS output
│   ├── get_surprisals.py           # Calculate sentence average surprisal
│   ├── get_linear_model.py         # Build linear regression model
│   ├── get_histogram.py            # Generate speech duration histogram
│
├── results/                        # Analysis results directory
│   ├── data.csv                    # Duration and surprisal data combination
│   ├── regression_plot.png 
│   ├── duration_histogram.png
│
├── README.md                       # Project description file
├── requirements.txt                # Python dependencies list
├── assignment_2_2024.pdf           # Assignment report
```

### **Environment Dependencies**

1. **Install Python and dependencies**:
   Ensure Python version is 3.8+, and install dependencies using the following command:

```bash
   pip install -r requirements.txt
```

2. **Install other tools**:
* **MAUS**: For processing speech data.
* **Praat**: For verifying speech duration calculation results.
* **ffmpeg**: For audio format conversion.

### **Running Steps**

1. **Calculate Information Content**:
   Use `scripts/get_surprisals.py` to extract Surprisal values for test sentences.
2. **Record Speech**:
* Record audio for the test sentences and store them in `data/recordings/`.
* Process the audio using MAUS and generate speech duration files.
3. **Data Processing and Analysis**:
* Use `scripts/get_durations.py` to calculate sentence durations.
* Use `scripts/get_linear_model.py` to build a linear regression model.
* Use `scripts/get_histogram.py` to visualize duration distribution.

## **Function Descriptions**

1. **get_durations.py**:
* Extract speech durations from MAUS output, output format is a dictionary.
2. **get_surprisals.py**:
* Train a bigram model.

* Calculate the average Surprisal of sentences.
3. **get_linear_model.py**:
* Use Pandas and Scikit-learn to build a linear regression model.

* Output regression coefficients, p-values, R² values, etc.
4. **get_histogram.py**:
* Plot a histogram of speech duration to show data characteristics.

## **References**

1. Jaeger, T. F., & Buz, E. (2017). Signal reduction and linguistic encoding. *The Handbook of Psycholinguistics*.
2. Kisler, T., Reichel, U., & Schiel, F. (2017). Multilingual processing of speech via web services. *Computer Speech & Language*.
