# -*- coding: utf-8 -*-
import time
import os
from model.lfm import LFM, Corpus

#改动这里的user_id，即可改推荐的目标用户（函数参数里的userid）
def run(userid):
    assert os.path.exists('data/ratings.csv'), \
        'File not exists in path, run preprocess.py before this.'
    print('Start..')
    start = time.time()
    if not os.path.exists('data/lfm_items.dict'):
        Corpus.pre_process()
    if not os.path.exists('data/lfm.model'):
        LFM().train()
    movies = LFM().predict(user_id=userid)
    #for movie in movies:
        #print(movie)
    print('Cost time: %f' % (time.time() - start))
    return movies
