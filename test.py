from pwperceptrons import pwperceptrons
from pwperceptrons import qd_pwperceptron
import copy


def insert_(item, val):
    item.append(val)
    return item

"""Basic Test"""
def test_():
    from datasets import load_yeast
    x, y = load_yeast()
    data = map(lambda n:insert_(n[0],n[1]), zip(x,y))
    pw = pwperceptrons(data, numeric_labels=False)
    print pw.classifiers
    return pw
