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

    def load_train_data(self):
        train_data = pd.read_csv(self.train_path, encoding='utf-8')
        return train_data

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
                user_i = [0, 0, 0, 0, 0, 0, 0, [], [], [], [], [], [], [], [], [], [], [], [], 0, 0]
                user_list = line.split('|')
                for i in user_list:
                    feature_i = i.split(' ')
                    if feature_i[0] == "uid":
                        user_i[0] = int(feature_i[1])
                    elif feature_i[0] == "age":
                        user_i[1] = int(feature_i[1])
                    elif feature_i[0] == "gender":
                        user_i[2] = int(feature_i[1])
                    elif feature_i[0] == "marriageStatus":
                        user_i[3] = int(feature_i[1])
                    elif feature_i[0] == "education":
                        user_i[4] = int(feature_i[1])
                    elif feature_i[0] == "consumptionAbility":
                        user_i[5] = int(feature_i[1])
                    elif feature_i[0] == "LBS":
                        user_i[6] = int(feature_i[1])
                    elif feature_i[0] == "interest1":
                        user_i[7] = [int(feature_i[x]) for x in range(1, len(feature_i))]
                    elif feature_i[0] == "interest2":
                        user_i[8] = [int(feature_i[x]) for x in range(1, len(feature_i))]
                    elif feature_i[0] == "interest3":
                        user_i[9] = [int(feature_i[x]) for x in range(1, len(feature_i))]
                    elif feature_i[0] == "interest4":
                        user_i[10] = [int(feature_i[x]) for x in range(1, len(feature_i))]
                    elif feature_i[0] == "interest5":
                        user_i[11] = [int(feature_i[x]) for x in range(1, len(feature_i))]
                    elif feature_i[0] == "kw1":
                        user_i[12] = [int(feature_i[x]) for x in range(1, len(feature_i))]
                    elif feature_i[0] == "kw2":
                        user_i[13] = [int(feature_i[x]) for x in range(1, len(feature_i))]
                    elif feature_i[0] == "kw3":
                        user_i[14] = [int(feature_i[x]) for x in range(1, len(feature_i))]
                    elif feature_i[0] == "topic1":
                        user_i[15] = [int(feature_i[x]) for x in range(1, len(feature_i))]
                    elif feature_i[0] == "topic2":
                        user_i[16] = [int(feature_i[x]) for x in range(1, len(feature_i))]
                    elif feature_i[0] == "topic3":
                        user_i[17] = [int(feature_i[x]) for x in range(1, len(feature_i))]
                    elif feature_i[0] == "ct":
                        user_i[18] = [int(feature_i[x]) for x in range(1, len(feature_i))]
                    elif feature_i[0] == "os":
                        user_i[7] = int(feature_i[1])
                    elif feature_i[0] == "carrier":
                        user_i[8] = int(feature_i[1])
                userFeature.append(user_i)
                print(user_i)
        userFeature = pd.DataFrame(np.array(userFeature), columns=["uid","age","gender","marriageStatus","education",
                                                     "consumptionAbility", "LBS","interest1","interest2","interest3",
                                                     "interest4","interest5","kw1","kw2","kw3","topic1","topic2",
                                                    "topic3","ct","os","carrier"])
        return userFeature

    def combine_train_data(self):
        adFeature = self.load_adFeature_data()
        train_data = self.load_train_data()
        userFeature = self.load_userFeature_data()

        data1 = pd.merge(train_data, adFeature, how='inner', on='aid')
        del data1['aid']
        data2 = pd.merge(data1, userFeature, how='inner', on='uid')
        del data2['uid']

        return data2


data_builder = DataBuilder()
train_data = data_builder.combine_train_data()
train_data.to_csv('../preliminary_contest_data/train_data_sample.csv')