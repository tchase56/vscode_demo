import matplotlib.pyplot as plt
import pandas as pd
from typing import Tuple
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def eval_metrics(actual: pd.DataFrame, pred: pd.DataFrame) -> Tuple[float, float, float]:
    '''
    determine metrics (rmse, mae, r2) from actuals and predictions

    Args:
        actual (pd.DataFrame): actual values of outputs
        pred (pd.DataFrame): predictions of outputs

    Returns:
        (tuple): tuple containing
            (float): root mean square error
            (float): mean absolute error
            (float): coefficient of determination
    '''
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2

def find_best_model(result_df:pd.DataFrame, metric: str)->Tuple[float, float]:
    '''
    determine the highest performing entry in a DF full of experiment results

    Args:
        result_df (pd.DataFrame): DF containing hyperparameters (alpha, l1) and metrics (RMSE, MAE, R2)
        metric (str): choose metric between RMSE, MAE, and R2

    Returns:
        (tuple): tuple containing
            (float): best apha parameter
            (float): best l1 parameter
    '''
    if metric not in ('RMSE', 'MAE', 'R2'):
        raise Exception('"metric" must be "rmse", "mae", or "r2"')

    if metric in ('RMSE', 'MAE'):
        best_metric = min(result_df[metric])
    elif metric == "R2":
        best_metric = max(result_df[metric])

    result_df_sub = result_df[result_df[metric] == best_metric].reset_index()
    alpha = result_df_sub.loc[0, "alpha"]
    l1 = result_df_sub.loc[0, "l1"]

    return alpha, l1


def plot_train_test_metrics(
    rmse_train: float,
    mae_train: float,
    r2_train: float,
    rmse_test: float,
    mae_test: float,
    r2_test: float
) -> None:
    '''
    plot the metrics (rmse, mae, r2) across the datasets (test, train)

    Args:
        rmse_train (float): root mean square error on training set
        mae_train (float): mean absolute error on training set
        r2_train (float): coefficient of determination on training set
        rmse_test (float): root mean square error on test set
        mae_test (float): mean absolute error on test set
        r2_test (float): coefficient of determination on test set

    Returns
        (pd.DataFrame): DF metric by dataset
    '''
    metric_df = pd.DataFrame(
        {
        "dataset": ['train', 'train', 'train', 'test', 'test', 'test'],
        "metric": ['rmse', 'mae', 'r2', 'rmse', 'mae', 'r2'],
        "value": [rmse_train, mae_train, r2_train, rmse_test, mae_test, r2_test]
        }
    )
    metric_df = metric_df.set_index(['metric', 'dataset']).unstack()
    metric_df = metric_df.droplevel(level=0, axis=1)

    metric_df.plot(kind='bar')
    plt.ylabel('Metric Value')
    plt.title('Performance Metrics')

    return metric_df
