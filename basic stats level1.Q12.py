# -*- coding: utf-8 -*-
"""
Created on Wed may 27 12:55:35 2022

@author: lalith kumar
"""

# stasts level1 Q12

import numpy as np
from matplotlib import pyplot as plt
x1 = np.array([34,36,36,38,38,39,39,40,40,41,41,41,41,42,42,45,49,56])

np.mean(x1)   # 41.0
np.median(x1) # 40.5
np.var(x1)    # 24.11111111111111
np.std(x1)    # 4.910306620885412

plt.hist(x1,color='b')
# from the above histogram we know that most of the students scored marks between (41 t0 42)

plt.boxplot(x1)
# from the above box plot we can identify the outliers as(49,56)
#--------------------------------------------------------------------------------
