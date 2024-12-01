import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import os

def fit_linear_model():
    # Prepare input and outputpath
    output_dir = "results"
    os.makedirs(output_dir, exist_ok=True)
    input_path = os.path.join(output_dir, "data.csv")
    output_path = os.path.join(output_dir, "regression_plot.png")
    
    # Load the data from 'data.csv'
    data = pd.read_csv('results/data.csv')

    # Apply logarithmic transformation to the duration column
    data['log_duration'] = np.log(data['duration'])

    # Prepare the independent variable (surprisal) and dependent variable (log duration)
    X = data['surprisal'].values.reshape(-1, 1)  # Convert the data to a two-dimensional array, as required by scikit-learn.
    y = data['log_duration'].values

    # Create and fit the linear regression model
    model = LinearRegression()
    model.fit(X, y)

    # Calculate R² value to assess the model's goodness of fit
    r_squared = model.score(X, y)

    # Use scipy.stats.linregress to compute linear regression statistics
    # slope: Rate of change of y with respect to X (regression line slope)
    # intercept: Value of y when X is zero (regression line y-intercept)
    # r_value: Correlation coefficient (-1 to 1), measures strength and direction of linear relationship
    # p_value: Probability that the slope is significantly different from zero 
    #            (small values indicate strong evidence of a relationship)
    # std_err: Standard error of the slope estimate 
    slope, intercept, r_value, p_value, std_err = stats.linregress(X.flatten(), y)  # Includes p-value

    # Print the regression metrics
    print(f"R² = {r_squared:.4f}")
    print(f"slope = {slope:.4f}")
    print(f"intercept = {intercept:.4f}")
    print(f"p-value = {p_value:.4f}")
    
    plot_regression(X, y, model, r_squared, p_value, output_path)


def plot_regression(X, y, model, r_squared, p_value, output_path):
    """Plot scatter plot and regression line with R² and p-value."""
    plt.figure(figsize=(10, 6))
    plt.scatter(X, y, alpha=0.5)
    plt.plot(X, model.predict(X), color='red', linewidth=2)

    plt.xlabel('Surprisal')
    plt.ylabel('Log Duration (s)')
    plt.title('Linear Regression: Log Duration vs Surprisal')

    # Add R² and p-value to the plot
    plt.text(0.05, 0.95, f'R² = {r_squared:.4f}\np = {p_value:.4f}',
             transform=plt.gca().transAxes)
    
    # Save and close
    plt.savefig(output_path)
    plt.close()


if __name__ == "__main__":
    fit_linear_model()
