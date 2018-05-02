# creator: Xu haonan
# date:2018/04/28
# function: read the large user feature data, and analysis each dimension of user feature

def user_feature(path):
    with open(path, 'r') as f:
        for line in f:
            print(line)


if __name__ == "__main__":
    user_feature("../preliminary_contest_data/userFeature.data")