from __future__ import division
import sys
import math
import random
from annsp import annsp
from types import FloatType, IntType
from functions import Functions

funcs_ = Functions()

sys.dont_write_bytecode = True

class pwperceptrons(object):
    """inits - some necessary preprocessing"""
    def __init__(self, data, numeric_labels=True, post_train_test=True):
        if self.verify_dimensions(data):
            self.post_train_test = post_train_test
            self.classifiers = {}
            random.shuffle(data)
            self.all_data = [a[:-1] for a in data]
            self.all_labels = [a[-1] for a in data]
            self.dmean_ = funcs_.mean_nm(self.all_data, axis=0)
            self.std_ = funcs_.std_nm(self.all_data, axis=0)
            self.all_data = funcs_.normalize_(self.all_data)
            
            if post_train_test:
                self.training_data = self.all_data[0:int(len(self.all_data)/100 * 90)]
                self.labels = self.all_labels[0:int(len(self.all_labels)/100 * 90)]
            
                self.test_data = self.all_data[int(len(self.all_data)/100 * 90):]
                self.test_labels = self.all_labels[int(len(self.all_labels)/100 * 90):]
            else:
                self.training_data  = self.all_data
                self.labels = self.all_labels
            
            h = {}
            for i in self.all_labels:
                if h.has_key(i):
                    h[i] += 1
                else:
                    h[i] = 1
            
            print "class distribution: %s" % h
            self.unique_labels = list(set(self.all_labels))
            
            if not numeric_labels:
                self.labels_map = dict([(n, i) for n,i in zip(self.unique_labels, range(1, len(self.unique_labels)+1))])
                self.unique_labels = map(lambda n: self.labels_map[n], self.unique_labels)
                self.labels  = map(lambda n: self.labels_map[n], self.labels)
                if post_train_test:
                    self.test_labels = map(lambda n: self.labels_map[n], self.test_labels)
            
            self.create_pairs()
    
    """verifying that the dimensions of dataset are accurate"""
    def verify_dimensions(self, data):
        random_pick = len(data[random.randrange(1, len(data))])
        if sum(map(len, data))/len(data) == random_pick:
            return True
        else:
            return False
    
    """returns N(N-1)/2 pairs/combinations of the classes involved"""
    def get_combinations(self, unique_labels):
        g = []
        for i, a in enumerate(unique_labels):
            current_ = unique_labels[i]
            for e, b in enumerate(unique_labels):
                if e > i:
                    g.append((unique_labels[i], unique_labels[e]))
        return g
    
    """returns all the data points which have the label/class equals to (a,b)"""
    def get_pair(self, pair_labels):
        set_data = []
        set_labels = []
        self.classifiers[pair_labels] = {}
        for i, j in enumerate(self.training_data):
            if self.labels[i] in pair_labels:
                set_data.append(self.training_data[i])
                set_labels.append(self.labels[i])
        return set_data, set_labels
        
    """creates multiple binary pairs based on the number of labels/classes"""
    def create_pairs(self):
        self.all_combinations = self.get_combinations(self.unique_labels)
        for i in self.all_combinations:
            pair_data, pair_labels = self.get_pair(i)
            #sending immediately for processing
            self.process(pair_data, pair_labels, i)
        if self.post_train_test:
            #test once the training for all the pairs is finished
            self.test_classifiers()
        
    """trains a neuron for the given data"""
    def process(self, set_data, set_labels, pair_label):
        self.classifiers[pair_label]['predictor'] = annsp(set_data, set_labels)

    def get_max(self, list_):
        h = {}
        for i in list_:
            if h.has_key(i):
                h[i] += 1
            else:
                h[i] = 1
        return max(h, key=h.get)

    """test_classifiers"""
    def test_classifiers(self):
        test =  {'true': 0, 'false': 0}
        for a,b in zip(self.test_data, self.test_labels):
            prediction = self.get_max(self.predict(a, True))
            real = b
            if prediction == real:
                test['true'] += 1
            else:
                test['false'] += 1
        print test
    
    """prediction method"""
    def predict(self, v, test_=False):
        results = []
        if not test_:
            for i, a in enumerate(v):
                v[i] = (v[i] - self.dmean_[i])/self.std_[i]
        for a in self.classifiers:
            classification = self.classifiers[a]['predictor'].classify(v)
            results.append(classification)
        if not test_:
            return self.get_max(results)
        else:
            return results
