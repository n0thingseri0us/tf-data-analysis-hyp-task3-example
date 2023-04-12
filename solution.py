import pandas as pd
import numpy as np
from scipy import stats
import math

chat_id = 371649437 # Ваш chat ID, не меняйте название переменной

def solution(control: np.array, test: np.array) -> bool:
    
     # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    # Ваш ответ, True или False
    alpha = 0.01

    res = (stats.ttest_ind(control, test, alternative = "two-sided").pvalue < alpha)
    return res
