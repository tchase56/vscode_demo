# Load Libraries
library(dplyr)
library(docstring)
source("/root/vscode_demo/R/R_functions.R")

# Read the wine-quality csv file from the URL
csv_url <- 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
data <- read.csv(csv_url, sep=';')
print(head(data))

# Correlation analysis
calculate_andPlot_correlation(data)