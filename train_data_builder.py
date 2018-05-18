# creator: Xu haonan
# date: 2018/04/28
# function: construct the training data (sampling method)
# input: train.csv; adFeature.csv; userFeature.csv;
# output: train_data_sample.csv (the input of LR, XGB .etc. models)

import pandas as pd
import numpy as np


class DataBuilder():
    def __init__(self):
        self.train_path = "../preliminary_contest_data/train.csv"
        self.test_path = "../preliminary_contest_data/train.csv"
        self.adFeature_path = "../preliminary_contest_data/adFeature.csv"
        self.userFeature_path = "../preliminary_contest_data/userFeature.data"
        self.sample = 1000

    def load_train_data(self):
        train_data = pd.read_csv(self.train_path, encoding='utf-8')
        return train_data.sample(self.sample)

    def load_test_data(self):
        test_data = pd.read_csv(self.test_path, encoding='utf-8')
        return test_data

    def load_adFeature_data(self):
        adFeature = pd.read_csv(self.adFeature_path, encoding='utf-8')
        return adFeature

    def load_userFeature_data(self):
        userFeature = []
        with open(self.userFeature_path, 'r') as f:
            for line in f:
                user_i = [0]*7
                user_list = line.split('|')
                for i in user_list:
                    feature_i = i.split(' ')
                    if feature_i[0] == "uid":
                        user_i[0] = feature_i[1]
                    elif feature_i[0] == "age":
                        user_i[1] = feature_i[1]
                    elif feature_i[0] == "gender":
                        user_i[2] = feature_i[1]
                    elif feature_i[0] == "marriageStatus":
                        user_i[3] = feature_i[1]
                    elif feature_i[0] == "education":
                        user_i[4] = feature_i[1]
                    elif feature_i[0] == "consumptionAbility":
                        user_i[5] = feature_i[1]
                    elif feature_i[0] == "LBS":
                        user_i[6] = feature_i[1]
                userFeature.append(user_i)
                print(user_i)
        userFeature = pd.DataFrame(np.array(userFeature), columns=["uid", "age", "gender", "marriageStatus", "education",
                                                     "consumptionAbility", "LBS"])
        return userFeature


dataBuild = DataBuilder()
adFeature = dataBuild.load_adFeature_data()
train_data = dataBuild.load_train_data()
userFeature = dataBuild.load_userFeature_data()
print(userFeature.head())

data1 = pd.merge(train_data, adFeature, how='inner', on='aid')
del data1['aid']
data2 = pd.merge(data1, userFeature, how='inner', on='uid')
del data2['aid']
del data2['uid']
print(data2.head())
