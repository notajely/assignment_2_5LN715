
# **Assignment 2 - Advanced Programming (5LN715)**

## **Project Overview**

This project is the second assignment for the **Advanced Programming (5LN715)** course at Uppsala University. It aims to study the relationship between speech clarity and information content (Surprisal) by analyzing speech duration and linguistic information content, verifying the hypothesis that speech clarity is positively correlated with information content.

---

## **Objectives**

1. **Data Processing**:

* Train a bigram model using `wiki.train.raw` data.
* Extract information content from `wiki.test.raw` data and generate sentence Surprisal values.

2. **Speech Data Collection**:

* Record speech data corresponding to the test sentences.
* Use **MAUS (Munich Automatic Segmentation System)** to extract phoneme durations.

3. **Analysis and Modeling**:

* Use a linear regression model to explore the relationship between speech clarity (duration) and information content (Surprisal).
* Visualize data using histograms and regression plots.

4. **Learning Goals**:

* Master modular programming, data processing, and analysis skills.
* Familiarize with speech and text data processing tools, such as MAUS and Python's data science libraries.

---

## **File Structure**

The project file structure is as follows:

```plaintext
assignment_2_5LN715/
│
├── data/                           # Data directory
│   ├── external/                   # Raw data: wiki.train.raw, wiki.test.raw
│   ├── processed/                  # Processed data: data.csv
│   ├── recordings/                 # Recording files (local storage only, not submitted)
│
├── scripts/                        # Core Python scripts
│   ├── get_durations.py            # Extract speech durations from MAUS output
│   ├── get_surprisals.py           # Calculate information content
│   ├── get_linear_model.py         # Build linear regression model
│   ├── get_histogram.py            # Generate speech duration histogram
│
├── results/                        # Analysis results directory
│   ├── plots/                      # Visualization results: histograms and regression plots
│   ├── models/                     # Saved regression model files
│
├── README.md                       # Project description file
├── requirements.txt                # Python dependencies list
├── .gitignore                      # Git ignore configuration
```

---

## **Installation and Running**

### **Environment Dependencies**

1. **Install Python and dependencies**:
   Ensure Python version is 3.8+, and install dependencies using the following command:

```bash
   pip install -r requirements.txt
```

2. **Install other tools**:

* **MAUS**: For processing speech data.
* **Praat**: For verifying speech duration calculation results.
* **ffmpeg or sox**: For audio format conversion.

### **Running Steps**

1. **Calculate Information Content**:
   Use `scripts/get_surprisals.py` to extract Surprisal values for test sentences.
2. **Record Speech**:

* Record audio for the test sentences and store them in `data/recordings/`.
* Process the audio using MAUS and generate speech duration files.

3. **Data Processing and Analysis**:

* Use `scripts/get_durations.py` to calculate word durations.
* Use `scripts/get_linear_model.py` to build a linear regression model.
* Use `scripts/get_histogram.py` to visualize duration distribution.

---

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

---

## **Example Output**

### **Linear Regression Model Results**:

* Regression Coefficient: `0.52`
* Intercept: `1.25`
* R² Value: `0.76`
* p-value: `< 0.001`

### **Visualization Charts**:

1. Speech Duration Histogram
2. Regression Scatter Plot of Information Content and Duration

---

## **Future Extensions**

1. Use more complex language models (e.g., GPT or Huggingface Transformers) to calculate information content.
2. Explore the performance of other languages or corpora in similar studies.
3. Introduce POS (Part of Speech) tags into the analysis to explore different patterns between function words and content words.

---

## **References**

1. Jaeger, T. F., & Buz, E. (2017). Signal reduction and linguistic encoding. *The Handbook of Psycholinguistics*.
2. Kisler, T., Reichel, U., & Schiel, F. (2017). Multilingual processing of speech via web services. *Computer Speech & Language*.

---

### **Repository Link**

GitHub: [assignment_2_5LN715](https://github.com/notajely/assignment_2_5LN715)
