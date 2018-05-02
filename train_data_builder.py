# creator: Xu haonan
# date: 2018/04/28
# function: construct the training data (sampling method)
# input: train.csv; adFeature.csv; userFeature.csv;
# output: train_data_sample.csv (the input of LR, XGB .etc. models)

import pandas as pd
import numpy as np


class DataBuilder():
    def __init__(self, sample_sum, ratio):
        self.train_path = "../preliminary_contest_data/train.csv"
        self.adFeature_path = "../preliminary_contest_data/adFeature.csv"
        self.userFeature_path = "../preliminary_contest_data/userFeature.data"
        self.sample_sum = sample_sum
        self.ratio = ratio

    def sampling_training_data(self):
        train_data = pd.read_csv(self.train_path, encoding='utf-8')
        positive_train_sample = train_data[train_data['label'] == 1]
        negative_train_sample = train_data[train_data['label'] == -1]
        sample_positive_train_sample = positive_train_sample.sample(self.sample_sum * self.ratio)
        sample_negative_train_sample = negative_train_sample.sample(self.sample_sum - self.sample_sum * self.ratio)

        sample_train_data = sample_positive_train_sample.append(sample_negative_train_sample)

        return sample_train_data

    def construct_feature_sample_data(self):
        sample_train_data = self.sampling_training_data()
        # use adFeature.csv and userFeature.data to complete the input data of Models
        feature_column_list = ['advertiserId', 'campaignId', 'creativeSize', 'adCategoryId',
                               'productId', 'productType', 'age', 'gender', 'marriageStatus',
                               'education', 'consumptionAbility', 'LBS', 'interest1', 'interest2',
                               'interest3', 'interest4', 'interest5', 'kw1', 'kw2', 'kw3',
                               'topic1', 'topic2', 'topic3', 'ct', 'os', 'carrier', 'house']
        ad_feature = pd.read_csv(self.adFeature_path, encoding='utf-8')
        for i in range(sample_train_data.shape[0]):
            aid = sample_train_data['aid'][i]
            uid = sample_train_data['uid'][i]
            aid_feature = ad_feature[ad_feature['aid'] == aid].values.toList()
