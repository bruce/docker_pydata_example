import pandas as pd
import numpy as np

class State:

    INITIAL_DATA = pd.DataFrame(data={'timestamp': [], 'value': []})

    def __init__(self, filename):
        self.filename = filename
        self.df = self.load()

    def load(self):
        try:
            return pd.read_pickle(self.filename)
        except FileNotFoundError:
            return self.INITIAL_DATA

    def append(self, data):
        self.df = self.df.append(data, ignore_index=True)

    def save(self):
        self.df.to_pickle(self.filename)

    def __str__(self):
        return self.df.__str__()
