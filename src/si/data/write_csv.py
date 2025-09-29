from si.data.dataset import Dataset
import pandas as pd
import numpy as np

def write_csv(filename: str, dataset: Dataset, sep: str = ",", features: bool = False, label: bool = False) -> None:
    """
    Writes a Dataset object to a CSV file

    Parameters
    ----------
    filename : str
        The path to the CSV file
    dataset : Dataset
        The Dataset object containing the data to be written
    sep : str, optional
        The separator used in the CSV file, by default ","
    features : bool, optional
        Whether to include the feature columns in the CSV file, by default none
    label : bool, optional
        Whether to include the label column in the CSV file, by default none

    Returns
    -------
    None
    """
    df = pd.DataFrame(dataset.X, columns=dataset.features)

    if features:
        df.columns = dataset.features
    
    if label:
        y = df.y = dataset.y
        label_name = dataset.label

    else:
        y= None
        label_name = None
    

    df.to_csv(filename, sep=sep, index=False)