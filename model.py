import pandas as pd
import numpy as np
import sklearn.preprocessing

class Model():
    def __init__(self):
        self.train_data_path = "../preliminary_contest_data/train_data_sample.csv"

    def generate_train_data(self):
        train_data = pd.read_csv(self.train_data_path, encoding='utf-8')
        y = train_data['label'].values
        del train_data['label']
        x = train_data.values
        # enc = sklearn.preprocessing.OneHotEncoder()
        # enc.fit(x)
        # x = enc.transform(x).toarray()

        return x, y

    def model_lr(self):
        x, y = self.generate_train_data()


