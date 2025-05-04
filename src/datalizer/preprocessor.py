import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def preprocess_data(X_train: pd.DataFrame, y_train: pd.DataFrame, merge_col: str, target_col: str, val: bool = False, test_size: float = 0.2, remove_corr: bool = False, corr_threshold: float = 0.95) -> tuple:
    """
    Merge the feature set (X_train) and target (y_train), optionally remove highly correlated features, and split the data into training and validation sets if specified.
    
    Parameters
    ----------
        X_train : pd.DataFrame
            Feature DataFrame.
        y_train : pd.DataFrame
            Target DataFrame.
        merge_col : str
            Column name to merge on.
        target_col : str
            Target column name.
        val : bool, optional
            Whether to split the data into training and validation sets (default is False).
        test_size : float, optional
            Proportion of the dataset to include in the validation split (default is 0.2).
        remove_corr : bool, optional
            Whether to remove highly correlated features (default is False).
        corr_threshold : float, optional
            Correlation threshold for feature removal (default is 0.95).
            
    Returns
    -------
        Touple
            If val is True, returns X_train_split, X_val_split, y_train_split, y_val_split, and dropped_corr_feats.
            If val is False, returns X_processed, y_processed, and dropped_corr_feats."""
    
    merged_data = pd.merge(X_train, y_train, on=merge_col)
    
    if remove_corr:
        X = merged_data.drop(columns=[target_col])
        corr_matrix = X.corr().abs()
        upper_tri = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
        dropped_corr_feats = [column for column in upper_tri.columns if any(upper_tri[column] > corr_threshold)]
        X = X.drop(columns=dropped_corr_feats)
        merged_data = pd.concat([X, merged_data[target_col]], axis=1)
        
    X_processed = merged_data.drop(columns=[target_col])
    y_processed = merged_data[target_col]
    
    if val:
        X_train_split, X_val_split, y_train_split, y_val_split = train_test_split(X_processed, y_processed, test_size=test_size, random_state=42)
        return X_train_split, X_val_split, y_train_split, y_val_split, dropped_corr_feats
    else:
        return X_processed, y_processed, dropped_corr_feats