# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 22:33:17 2020

@author: Jinhong Chan
"""


import pandas as pd
import recallprocess
import dataprocess
import w2v4callactor

def recommender_movie_recall(user_id = None, k = 5, use_actor = {"topK":1, "limitpactor":1}):
    
    
    result = {}
    
    # 使用svd模型基于评分预测召回topk评分预测的电影
    algo_svd = recallprocess.svd4_user_movie_rate()
    user_movie = dataprocess.user_movie().loc["user_id" == user_id,:]
    user_movie["predictrate"] = user_movie.apply(lambda x:algo_svd.predict(x.user_id, x.movie_id), axis=1)
    result["TopKmoviebysvd"] = list(user_movie.sort_values(by = "predictrate", ascending = False).loc[0:(k-1),:]["movie_id"])
    
    # 按用户可能喜欢的演员的相似演员推荐
    algo_w2v_actor = w2v4callactor.w2v_casts()
    df_user_actor_rate = dataprocess.create_user_actor_rate().loc["user_id" == user_id, :].sort_values(by = "rate", ascending = False)
    actor_topk_list = list(df_user_actor_rate.loc[0:(use_actor["topK"]-1), "actor_id"])
    result["byactor"] = [{x:algo_w2v_actor.most_similar(x,topn = use_actor["limitpactor"])} for x in actor_topk_list]
    
    return result