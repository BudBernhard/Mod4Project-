"""
DOCSTRING: This module contains the different values we used in gridsearch to optimize hyperparamters for various models. 

"""

from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report


def find_hyperparameters(pipe, params, X_train, y_train):
    
    res = GridSearchCV(pipe, params, scoring = 'f1', return_train_score = True)
    res.fit(X_train, y_train)
    
    return res




pipe_dt = Pipeline([('dt', DecisionTreeClassifier())])
params_dt = {'dt__max_depth': [2, 4, 8],
                'dt__min_samples_leaf':[50, 80]}


pipe_rf = Pipeline([('rf', RandomForestClassifier())])
params_rf = {'rf__n_estimators': [10, 30],
                 'rf__min_samples_leaf': [20, 50, 70],
                 'rf__max_features': ['log2', 'sqrt']}

pipe_svc = Pipeline([('svc', SVC(kernel = 'rbf'))])
params_svc = {'svc__C': [0.1, 1, 10, 100]},

pipe_knn = Pipeline([('knn', KNeighborsClassifier())]),
params_knn = {'knn__n_neighbors':[2,4,8,16],
                'knn__p':[2,3]}
