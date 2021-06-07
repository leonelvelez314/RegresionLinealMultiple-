import pandas as pd
import matplotlib as plt
import numpy as np
from sklearn import datasets, linear_model



data_set = datasets.load_boston()
data  =  pd.DataFrame(np.c_[data_set["data"]], columns=data_set["feature_names"])


