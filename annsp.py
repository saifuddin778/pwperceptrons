from __future__ import division
import random
import math
import sys
import numpy
from compiler.ast import flatten
sys.dont_write_bytecode = True

class annsp(object):
    def __init__(self, data, labels):
        if self.verify_dimensions(data):
            self.x = data
            self.y = labels
            self.unique_labels = sorted(list(set(self.y)))
            self.weights = list(numpy.random.normal(scale=0.01, size=len(data[0])+1))
            self.eta = 0.01
            self.train()
        else:
            print 'dimensions inaccurate'
    
    def verify_dimensions(self, x):
        random_pick = len(x[random.randrange(1, len(x))])
        if sum(map(len, x))/len(x) == random_pick:
            return True
        else:
            return False

    def adder(self, w, v):
        #return math.tanh(sum([i*j for i,j in zip(w,v)]))
        add_ = sum([i*j for i,j in zip(w,v)])
        return 1/(1+math.exp(-add_))

    def signum(self, val):
        if val >= 0.5:
            #return 1
            return self.unique_labels[1]
        else:
            #return -1
            return self.unique_labels[0]

    def scalar_prod(self, v, s):
        r = []
        for i in range(0, len(v)):
            r.append(s*v[i])
        return r
    
    def vector_adapt(self, w, x, ex, d):
        vector_sum = lambda x,y: [a+b for a,b in zip(x,y)]
        diff = self.scalar_prod(x, self.eta*(ex-d))
        updated_weights = vector_sum(w, diff)
        return updated_weights

    def train(self):
        temp_train= []
        for i in range(0, len(self.x)):
            temp_train.append(flatten([self.y[i], self.x[i]]))
        
        for i in range(0, 10):
            for j in range(0, len(temp_train)):
                expected_decision = self.y[j]
                decision = self.signum(self.adder(self.weights, temp_train[j]))
                while decision != expected_decision:
                    self.weights = self.vector_adapt(self.weights, temp_train[j], expected_decision, decision)
                    decision = self.signum(self.adder(self.weights, temp_train[j]))
    
    def classify(self, v):
        g = [0]
        for i in v:
            g.append(i)
        decision = self.signum(self.adder(self.weights, g))
        return decision
