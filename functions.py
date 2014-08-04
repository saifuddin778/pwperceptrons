from __future__ import division
import sys
sys.dont_write_bytecode = True
import math
import random
import gc

class Functions(object):
    def __init__(self):
        return
    
    #flatten an array
    def flatten(self, x, out_):
        for a in x:
            if type(a) == type([]):
                out_ = self.flatten(a, out_)
            else:
                out_.append(a)
        return out_
    
    #mean of an array
    def mean_(self, x):
        return float(sum(x))/len(x)

    #standard deviation of an array
    def std_(self, x):
        m_x = self.mean_(x)
        return math.sqrt(sum([math.pow((a-m_x), 2) for a in x])/len(x))

    #mean of a n x m array with axis defined (1 being row wise mean, 0 being column wise,
    #and no axis definition means for the flattened array/matrix
    def mean_nm(self, x, axis=False):
        if axis == 0:
            return map(self.mean_, zip(*x))
        elif axis == 1:
            return map(self.mean_, x)
        elif not axis:
            return self.mean_(self.flatten(x, []))
        else:
            return False

    #standard deviation of a n x m array with axis defined (1 being row wise, 0 being column wise,
    #and no axis definition means for the flattened array/matrix
    def std_nm(self, x, axis=False):
        if axis == 0:
            return map(self.std_, zip(*x))
        elif axis == 1:
            return map(self.std_, x)
        elif not axis:
            return self.std_(self.flatten(x, []))
        else:
            return False

    def normalize_1d(self, x):
        k = []
        x_mean = self.mean_(x)
        for a in x:
            k.append(a-x_mean)
        l = []
        x_std = self.std_(x)
        for a in k:
            l.append(float(a)/x_std)

        return l
        
        
    def normalize_(self, x):
        #data -= data.mean(axis=0)
        k = []
        x_mean = self.mean_nm(x, axis=0)
        for a in range(0, len(x)):
            l =[]
            for b in range(0, len(x[a])):
                l.append(float(x[a][b]) - float(x_mean[b]))
            k.append(l)
        
        #data /= data.std(axis=0)
        l_ = []
        x_std = self.std_nm(k, axis=0)
        for a in range(0, len(k)):
            g = []
            for b in range(0, len(k[a])):
                g.append(float(float(k[a][b]) / float(x_std[b])))
            l_.append(g)
        return l_
