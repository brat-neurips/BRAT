from BRAT.algorithms import BRATD
from BRAT.utils import generate_data
Xtr,ytr,Xte,yte,_ = generate_data('friedman1', n_train=100, n_test=10, seed=0)
m = BRATD(n_estimators=10, learning_rate=0.3, dropout_rate=0.3,
          subsample_rate=0.8, max_depth=2)
m.fit(Xtr, ytr, Xte, yte)
assert m.predict(Xte).shape == (10,)
