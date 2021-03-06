# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 17:40:04 2020

@author: Administrator
"""

import os

from surprise import Dataset
from surprise import Reader
from surprise import KNNBaseline
from surprise import SVD
from surprise import dump

import dataprocess



DATA_BASE_PATH = "../dataset"
USER_MOVIE_RATE_PATH = "/user_movie_rate.csv"

SIM_OPTIONS_KNN = "pearson"
N_EPOCHS_SVD = 37
LR_ALL_SVD = 0.005

ALGO_RESULT_PATH = "../algoresultrapo"
KNN_RESULT_USER2MOVIE = "/knnresultuser2movie" # knn算法召回电影
SVD_RESULT_USER2MOVIE = "/svdresultuser2movie" # svd方法召回电影
SVD_RESULT_USER2ACTOR = "/svdresultuser2actor" # svd方法召回演员
SVD_RESULT_USER2DIRECTOR = "/svdresultuser2director" # svd方法召回导演
SVD_RESULT_USER2AREA = "/svdresultuser2area" # svd方法召回地区
W2V_RESULT_USER2COMMENT = "/w2vresultuser2coment" # w2v方法召回评论



def svd4_user_movie_rate():
    """

    Returns
    -------返回训练好的基于user movie rating数据的svd模型，若没有训练好的模型存储，则触发模型训练&保存
    TYPE
        surprise.prediction_algorithms.algo_base.AlgoBase.
    TYPE
        surprise算法对象.

    """
    
    if os.path.exists(ALGO_RESULT_PATH + SVD_RESULT_USER2MOVIE):
        return dump.load(ALGO_RESULT_PATH + SVD_RESULT_USER2MOVIE)[0]
    else:
        # 读取数据
        reader = Reader(line_format = "user item rating")
        data = Dataset.load_from_df(dataprocess.create_user_movie_rate().loc[:,["user","movie","rate"]], reader = reader)
        trainset = data.build_full_trainset()
        
        # 参数设置&模型初始化
        algo = SVD(n_epochs=N_EPOCHS_SVD, lr_all=LR_ALL_SVD, verbose=True)
        algo.fit(trainset)
        
        dump.dump(file_name = ALGO_RESULT_PATH + SVD_RESULT_USER2MOVIE, 
                  algo = algo, verbose = True)
        return algo


def knn_user_movie_rate():
    """

    Returns
    -------返回训练好的基于user movie rating数据的knnbaseline模型
    TYPE
        surprise.KNNbaseline object.

    """
    
    if os.path.exists(ALGO_RESULT_PATH + KNN_RESULT_USER2MOVIE):
        return dump.load(ALGO_RESULT_PATH + KNN_RESULT_USER2MOVIE)[0]
    else:
        # 读取数据
        reader = Reader(line_format = "user item rating", sep = ",")
        data = Dataset.load_from_df(dataprocess.create_user_movie_rate().loc[:,["user","movie","rate"]], reader = reader)
        trainset = data.build_full_trainset()
        
        # 参数设置&模型初始化
        sim_options = {'name': 'pearson', "user_based":False}
        algo = KNNBaseline(k = 10, sim_options = sim_options)
        algo.fit(trainset)
        
        dump.dump(file_name = ALGO_RESULT_PATH + KNN_RESULT_USER2MOVIE, 
                  algo = algo, verbose = True)
        return algo


def svd4_user_actor_rate():
    """

    Returns
    -------返回训练好的基于user actor rating数据的svd模型，若没有训练好的模型存储，则触发模型训练&保存
    None.

    """


if __name__ == "__main__":
    svd4_user_movie_rate()
