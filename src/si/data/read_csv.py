from si_SI.src.si.data.dataset import Dataset
import pandas as pd
import numpy as np

def read_csv(filename: str, sep: str, label: bool = False, features : bool = False) -> Dataset:
    """
    Reads a CSV file and returns a Dataset object
    Parameters
    ----------
    filename : str
        The path to the CSV file
    sep : str, optional
        The separator used in the CSV file, by default ","
    label : bool, optional
        Whether the CSV file has a label column, by default True
    Returns
    -------
    Dataset
        The Dataset object containing the data from the CSV file
    """
    pass

    df = pd.read_csv(filename, sep=sep)

    if features and label:
        x = df.iloc[:,:-1].to_numpy()
        y = df.iloc[:,-1].to_numpy()
        feature_names = df.columns = df.columns[:-1]
        label_name = df.columns[-1]
        return Dataset(X=x, y=y, features=feature_names, label=label_name)
    elif features and not label:
        x = df.to_numpy()
        feature_names = df.columns
        return Dataset(X=x, features=feature_names)
    elif label:
        x = np.array()
        y = df.iloc[:,-1].to_numpy()
        label_name = df.columns[-1]
        return Dataset(X=x, y=y, label=label_name)
    else:
        return None