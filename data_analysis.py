# creator: Xu haonan
# date: 2018/04/28
# functions: analysis the positive and negative samples;
#            count each aid's instances

import pandas as pd
import numpy as np

def sample_anaysis(path):
    data = pd.read_csv(path, encoding='utf-8')
    print(data.shape)
    positive_count = 0
    negative_count = 0
    for i in range(data.shape[0]):
        if data['label'][i] == 1:
            positive_count += 1
        else:
            negative_count += 1

    print(positive_count, negative_count)

def ads_feature_analysis(train_path, ad_feature_path):
    train_data = pd.read_csv(train_path, encoding='utf-8')
    ad_feature = pd.read_csv(ad_feature_path, encoding='utf-8')
    aid = (ad_feature['aid'].values).tolist()
    print(train_data.shape)
    D = dict(zip(aid, [0 for x in range(0, len(aid))]))
    for i in range(train_data.shape[0]):
        D[train_data['aid'][i]] += 1

    df = pd.DataFrame(D, index=[0])
    df.to_csv("./adfeature_count.csv", encoding='utf-8')
    print(df)


if __name__ == "__main__":
    #sample_anaysis("../preliminary_contest_data/train.csv")
    ads_feature_analysis("../preliminary_contest_data/train.csv","../preliminary_contest_data/adFeature.csv")