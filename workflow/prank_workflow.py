# -*- coding: utf-8 -*-
import time
import os
from model.prank import Graph, PersonalRank

#改动这里的user_id，即可改推荐的目标用户
def run(userid):
    assert os.path.exists('data/ratings.csv'), \
        'File not exists in path, run preprocess.py before this.'
    print('Start..')
    start = time.time()
    if not os.path.exists('data/prank.graph'):
        Graph.gen_graph()
    if not os.path.exists('data/prank_'+str(userid)+'.model'):
        PersonalRank().train(user_id=userid)
    movies = PersonalRank().predict(user_id=userid)
    #for movie in movies:
        #print(movie)
    print('Cost time: %f' % (time.time() - start))
    return movies
