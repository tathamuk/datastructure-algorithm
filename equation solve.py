# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 15:58:43 2018

@author: 1000248451
"""

import sympy as sy 
import numpy as np
x, y = sy.symbols('x y')
y=sy.simplify(-800 + 80*800*3*x + 3*((x)**2))
print(y)
coeff=(-800, 19200, 3)
print(np.roots(coeff))