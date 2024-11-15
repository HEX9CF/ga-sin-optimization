import numpy as np

# 目标函数
def objective_function(x, j):
    return 3 - np.sin(j * x[0])**2 - np.sin(j * x[1])**2
