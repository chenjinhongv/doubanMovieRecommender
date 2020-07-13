# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 17:11:37 2020

@author: Administrator
"""


import os
import pandas as pd
import json

BASE_PATH = "../dataset"
USER_RATE = "/DMSC.csv"
MOVIE = "/movie.json"


# 产出USER MOVIE RATE TIMESTAMP数据
def create_user_movie_rate(infile=BASE_PATH + USER_RATE, outfile=BASE_PATH + "/user_movie_rate.csv"):
    
    if os.path.exists(outfile):
        pass
    else:
        rate = pd.read_csv(infile)
        rate = rate.loc[rate.Username != "[已注销]",["Username","Movie_Name_CN","Star","Date"]]
        rate = rate.rename(columns = {"Username":"user","Movie_Name_CN":"movie","Star":"rate","Date":"timestramp"})
        rate.to_csv(outfile, index=False, header=False)


# 产出MOVIE CASTS 数据
def create_movie_actor(infile=BASE_PATH + MOVIE, outfile=BASE_PATH + "/movie_actor_list.json"):
    """

    Returns
    -------
    电影的演员表列表
        [[actorname1：actorname2：...],[actorname1：actorname2：...],...] 
    保存演员列表为json文件
    None.

    """
    
    casts = []
    if os.path.exists(outfile):
        with open(outfile, "r", encoding="utf-8") as f:
            casts = json.loads(f.readline())
    else:
        for line in open(infile, "r", encoding="utf-8"):
            try:
                cast = json.loads(line)["casts"]
                cast = [x["name"] for x in cast]
                casts.append(cast)
            except  Exception:
                pass
        
        json_casts = json.dumps(casts)
        with open(outfile, "w") as f:
            f.write(json_casts)
    
    return casts


# 产出MOVIE DIRECTOR RATE TIMESTRAMP 数据
def create_movie_
        
        


#
if __name__ == "__main__":
    create_movie_actor()