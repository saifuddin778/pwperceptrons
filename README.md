pwperceptrons
=============
Pairwise coupling of multiple perceptrons to form a rich multi-label prediction model.

Based on the works done by [Chen et, al.](http://www.contrib.andrew.cmu.edu/~fchen1/On_Locally_Linear_Classification_by_Pairwise_Coupling.pdf) and [Mencia & Furnkranz](https://www.ke.tu-darmstadt.de/~juffi/publications/ijcnn-08.pdf), this is a naive implementation of pairwise coupling of perceptrons, which are interlinked for the purpose of classification of multi-label datasets.

####Usage:
To use the pairwise coupling of perceptrons alone:
```python
>>> from pwperceptrons import pwperceptrons
>>> data = [[p1, p2, p3, class], [p1, p2, p3, class]....[p1, p2, p3, class]]
>>> pw = pwperceptron(data, numeric_labels=True, post_train_test=True)
>>> pw.predict([p1, p2, p3])
>>> ...
```
To use a QDA layer at the top of the pairwise coupling:
```python
>>> from pwperceptrons import qda_pwperceptrons
>>> data = [[p1, p2, p3, class], [p1, p2, p3, class]....[p1, p2, p3, class]]
>>> qdp = qda_pwperceptrons(data)
>>> qdp.predict([p1, p2, p3])
>>> ...
```
#####Parameters:
* `numeric_labels` => by default `True` to assume that class labels are numeric. Set to `False` if class labels are non-numeric.
* `post_train_test` => by default `True` to reserve 10% of the training data for testing. Set to `False` in order to avoid.
