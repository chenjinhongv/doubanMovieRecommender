# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 17:11:37 2020

@author: Administrator
"""


import os
import pandas as pd

BASE_PATH = "../dataset"
USER_RATE = "/DMSC.csv"
MOVIE = "/movie.json"


# 产出USER MOVIE RATE TIMESTAMP数据
def create_user_movie_rate():
    
    if os.path.exists(BASE_PATH + "/user_movie_rate.csv"):
        pass
    else:
        rate = pd.read_csv(BASE_PATH + USER_RATE)
        rate = rate.loc[rate.Username != "[已注销]",["Username","Movie_Name_CN","Star","Date"]]
        rate = rate.rename(columns = {"Username":"user","Movie_Name_CN":"movie","Star":"rate","Date":"timestramp"})
        rate.to_csv(BASE_PATH + "/user_movie_rate.csv", index=False, header=False)



#
if __name__ == "__main__":
    create_user_movie_rate()