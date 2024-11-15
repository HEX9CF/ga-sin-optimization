import numpy as np

# 目标函数
def objective_function(x):
    return 3 - np.sin(2 * x[0])**2 - np.sin(2 * x[1])**2
