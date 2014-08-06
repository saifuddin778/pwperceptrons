pwperceptrons
=============
Pairwise coupling of multiple perceptrons to form a rich multi-label prediction model.

Based on the works done by [Chen et, al.](http://www.contrib.andrew.cmu.edu/~fchen1/On_Locally_Linear_Classification_by_Pairwise_Coupling.pdf) and [Mencia & Furnkranz](https://www.ke.tu-darmstadt.de/~juffi/publications/ijcnn-08.pdf), this is a naive implementation of pairwise coupling of perceptrons, which are interlinked for the purpose of classification of multi-label datasets.

There are two main methods existing for now:

* A classifier can be generated using simply the pairwise coupling alone i.e. training `N(N-1)/2` number of cassifiers (where `N` is the number of classes involved) to do the prediction, where the result is selected using the voting system.
* A classifier that utilizes a [QDA](https://onlinecourses.science.psu.edu/stat557/node/43) predictor layer at the top can be added within the scenario, which basically gives the top two possible classes `(ci, cj)` for the given input, and then utilizes the exact classifier trained on the particular couple to do the prediction. In this way, not only the complexity is reduced but the overall precision is increased as well. However, this particular method do require that almost equal number of instances are provided for each class during the training.

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
