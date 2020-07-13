# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 23:30:28 2020

@author: Administrator
"""


import os
import multiprocessing
import gensim

import dataprocess



ALGO_RESULT_PATH = "../algoresultrapo"
W2V_RESULT_ACTOR2MOVIE = "/w2vresultactor2movie.model" # w2v方法召回相似演员


# 对演员列表数据进行W2V建模
def w2v_casts(modelfile=ALGO_RESULT_PATH + W2V_RESULT_ACTOR2MOVIE, retrain = False):
    """

    Parameters
    ----------
    modelfile : TYPE, optional
        DESCRIPTION. The default is ALGO_RESULT_PATH + W2V_RESULT_ACTOR2MOVIE.
    retrain : TYPE, optional
        if True ,will retrain the model and return.if False and exist trained model,load the model and return it  The default is False.

    Returns
    -------trained w2v model
    model : TYPE
        gensim.models.Word2Vec object.

    """
    
    if os.path.exists(modelfile) & (retrain == False):
        model = gensim.models.Word2Vec.load(modelfile)
    else:
        # 删除模型
        try:
            os.remove(modelfile)
        except FileNotFoundError:
            pass
        
        # 重新训练并保存模型
        cores = multiprocessing.cpu_count() # 调用所有核心资源
        casts = dataprocess.create_movie_actor()
        model = gensim.models.Word2Vec(sentences=casts, size=50, min_count=2, window=7, workers=cores)
        model.save(modelfile)
    
    return model
        
            
if __name__ == "__main__":
    w2v_casts()