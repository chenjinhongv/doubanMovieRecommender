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


# 处理DMSC.csv数据集，产出USER MOVIE RATE TIMESTAMP数据
def create_user_movie_rate(infile=BASE_PATH + USER_RATE, outfile=BASE_PATH + "/user_movie_rate.csv"):
    
    if os.path.exists(outfile):
        rate = pd.read_csv(args, kwargs)
    else:
        rate = pd.read_csv(infile)
        rate = rate.loc[rate.Username != "[已注销]",["Username","Movie_Name_CN","Star","Date"]]
        rate = rate.rename(columns = {"Username":"user","Movie_Name_CN":"movie","Star":"rate","Date":"timestramp"})
        rate.to_csv(outfile, index=False, header=True)
    
    return rate


# 处理movie.json数据,生成csv文件
def movie2csv(outfile=BASE_PATH + "/movie.csv"):
    """

    Parameters
    ----------
    outfile : TYPE, optional
        电影数据保存路径. The default is BASE_PATH + "/movie.csv".

    Returns
    -------
    df_movie_info : pandas.DataFrame
        电影信息数据框.
        moviename：电影名
        anothermoviename：电影别名
        ratingpeople：评论人数
        avgrating：平均评分
        country：国家（多个国家取第一个）
        director：导演
        summary：电影简介
        duration：电影片长，单位hour
        year：电影年份
    """
    
    if os.path.exists(outfile):    # 若存在已生成的csv文件，直接从csv文件导出数据生成数据框返回 
        
        df_movie_info = pd.read_csv(outfile)
        
    else:    # 重新处理数据
        
        movie_dict_list = []
        
        for line in open(BASE_PATH + MOVIE, "r", encoding="utf-8"):
            try:
                
                ori_movie_dict = json.loads(line)
                new_movie_dict = {}
                
                new_movie_dict["moviename"] = ori_movie_dict["title"]
                new_movie_dict["ratingpeople"] = ori_movie_dict["rating"]["rating_people"]
                new_movie_dict["avgrating"] = ori_movie_dict["rating"]["average"]
                new_movie_dict["country"] = ori_movie_dict["countries"][0]
                new_movie_dict["director"] = ori_movie_dict["directors"][0]["name"]
                new_movie_dict["summary"] = ori_movie_dict["summary"]
                new_movie_dict["language"] = ori_movie_dict["languages"][0]
                new_movie_dict["duration"] = ori_movie_dict["duration"]
                new_movie_dict["year"] = ori_movie_dict["year"]
                new_movie_dict["anothermoviename"] = ori_movie_dict["aka"][0]
                
                movie_dict_list.append(new_movie_dict)
                
            except  Exception:
                pass
        
        df_movie_info = pd.DataFrame(movie_dict_list)
        df_movie_info.to_csv(outfile, index=False, header=True)
    
    return df_movie_info


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

<<<<<<< HEAD
=======

# 产出USER ACTOR RATE 数据
def create_user_actor_rate(outfile):
    pass

# 产出USER MOVIE 数据
def create_user_movie(outfile):
    pass
>>>>>>> 30e1be8293c80c6590a3443ad684ea472a25db54


# 产出USER DIRECTOR RATE 数据
def create_user_director_rate(outfile=BASE_PATH + "/movie/actor"):
    
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
    
    
    
        
        


#
if __name__ == "__main__":
    pass