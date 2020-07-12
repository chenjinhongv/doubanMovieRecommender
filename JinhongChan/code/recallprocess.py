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



BASE_PATH = "../dataset"
USER_MOVIE_RATE_PATH = "/user_movie_rate.csv"

SIM_OPTIONS_KNN = "pearson"
N_EPOCHS_SVD = 37
LR_ALL_SVD = 0.005

ALGO_PATH = "../algoresultrapo"
SVD_RESULT_PATH = "/svdresult"
KNN_RESULT_PATH = "/knnsesult"



def get_svd():
    """

    Returns
    -------返回训练好的svd模型结果（元组）0：（模型， 模型预测结果）
    TYPE
        truple.
    TYPE
        DESCRIPTION.

    """
    
    if os.path.exists(ALGO_PATH + SVD_RESULT_PATH):
        return dump.load(ALGO_PATH + SVD_RESULT_PATH)
    else:
        reader = Reader(line_format = "user item rating timestramp", sep = ",")
        data = Dataset.road_from_file(BASE_PATH + USER_MOVIE_RATE_PATH, reader = reader)
        trainset = data.build_full_trainset()
        
        algo = SVD(n_epochs=N_EPOCHS_SVD, lr_all=LR_ALL_SVD, verbose=True)
        algo.fit(trainset)
        
        dump.dump(file_name = ALGO_PATH + SVD_RESULT_PATH, predictions = algo.predictions,
                  algo = algo, verbose = True)
        return (algo, algo.predictions)


if __name__ = "__main__":
    get_svd()
