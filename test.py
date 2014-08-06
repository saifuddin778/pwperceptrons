from pwperceptrons import pwperceptrons
from pwperceptrons import qda_pwperceptrons
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
    return pw


def test_qda():
    test = {'true': 0, 'false': 0}
    from datasets import load_seeds
    x, y = load_seeds()
    data = map(lambda n:insert_(n[0],n[1]), zip(x,y))
    qdp= qda_pwperceptrons(data)

    for i in range(0, len(x)):
        prediction = qdp.predict(x[i][:-1])
        real =  y[i]
        if prediction == real:
            test['true'] += 1
        else:
            test['false'] += 1
    return test

print test_qda()
