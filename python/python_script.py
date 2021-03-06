# First, train a linear regression model that takes two hyperparameters: alpha and l1_ratio.

# This example uses the familiar pandas, numpy, and sklearn APIs to create a simple machine learning model.

# You can run the example through the .py script using the following command.
# python python_script.py <alpha> <l1_ratio>

import sys
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
from python_functions import eval_metrics, plot_train_test_metrics

if __name__ == "__main__":
    np.random.seed(40)

    # Read the wine-quality csv file from the URL
    csv_url =\
        'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
    data = pd.read_csv(csv_url, sep=';')

    # Split the data into training and test sets. (0.75, 0.25) split.
    train, test = train_test_split(data)

    # The predicted column is "quality" which is a scalar from [3, 9]
    train_x = train.drop(["quality"], axis=1)
    test_x = test.drop(["quality"], axis=1)
    train_y = train[["quality"]]
    test_y = test[["quality"]]

    alpha = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
    l1_ratio = float(sys.argv[2]) if len(sys.argv) > 2 else 0.5

    lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=42)
    lr.fit(train_x, train_y)

    train_predictions = lr.predict(train_x)
    test_predictions = lr.predict(test_x)
    (rmse_train, mae_train, r2_train) = eval_metrics(train_y, train_predictions)
    (rmse_test, mae_test, r2_test) = eval_metrics(test_y, test_predictions)

    print("Elasticnet model (alpha=%f, l1_ratio=%f):" % (alpha, l1_ratio))
    print("  Train RMSE: %s" % rmse_train)
    print("  Train MAE: %s" % mae_train)
    print("  Train R2: %s" % r2_train)
    print("  Test RMSE: %s" % rmse_test)
    print("  Test MAE: %s" % mae_test)
    print("  Test R2: %s" % r2_test)

    # Plot Visualization of Metrics
    df = plot_train_test_metrics(rmse_train, mae_train, r2_train, rmse_test, mae_test, r2_test)
    print(df)