from sklearn.base import BaseEstimator, TransformerMixin


class ColumnAdder(BaseEstimator, TransformerMixin):
    """Simple class that allows you to specify which two columns you want to add.
    """

    def __init__(self, columns, newName):
        self.columns = columns
        self.newName = newName

    def transform(self, X, y=None):
        X[self.newName] = X[self.columns[0]] + X[self.columns[0]]
        return X

    def fit(self, X, y=None):
        return self

