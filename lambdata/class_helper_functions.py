"""Module of Data Science helper functions"""

import pandas as pd
from sklearn.utils import shuffle


def null_count(df):
    """Check a DataFrame for null values and returns the number of missing
    values"""
    return df.isna().sum().sum()


def null_count_alt(df):
    """Check a Dataframe for null values and returns the number of missing
    values"""
    x = [df[col].isna().sum() for col in df.columns]
    y = 0
    for _ in x:
        y += _
    return y


def train_test_split(df, frac):
    """Create a train/test split function for a data frame that returns both the
    training and test sets.  'frac' refers to the percent of data you would
    like to set aside for training"""
    cutoff = df.index < int(df.shape[0] * frac)
    df_train = df.loc[cutoff]
    df_test = df.loc[~cutoff]
    return df_train, df_test


def randomize(df, seed=None):
    """Develop a randomization function that randomizes all of a dataframe's cells
    then returns that randomized dataframe.  This function also accepts a
    random seed for reproducible randomization"""
    df = df.copy()
    columns = df.columns
    df = shuffle(df[columns], random_state=seed)
    return df