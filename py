#!/usr/bin/env bash
    # --matplotlib=tk \
exec python3 -mIPython \
    --no-confirm-exit \
    --no-banner \
    --nosep \
    -i \
    -c "

# Math and science
try:
    import numpy as np
except ModuleNotFoundError as e:
    pass

try:
    import scipy; from scipy.special import binom, factorial, comb, perm
except ModuleNotFoundError as e:
    pass

import random; from random import *
import math; from math import *
import statistics; from statistics import *

try:
    import matplotlib.pyplot as plt; from matplotlib.pyplot import *
except ModuleNotFoundError as e:
    pass

try:
    import sympy; from sympy import Symbol, var, symbols, Matrix, solve
except ModuleNotFoundError as e:
    pass

# Generic
import itertools; from itertools import *
import functools; from functools import reduce, partial, partialmethod, singledispatch, cache
import collections; from collections import *
import pickle

# System
import json
import sys
import os
import time; from time import sleep
from pathlib import Path

# Misc
try :
    from forex_python.converter import CurrencyRates
    usd = cache(lambda dest_currency='RUB': CurrencyRates().get_rate('USD', dest_currency))
    eur = cache(lambda dest_currency='RUB': CurrencyRates().get_rate('EUR', dest_currency))
except ModuleNotFoundError as e:
    pass

HOME = Path('~').expanduser()

segment = lambda a, b: range(a, b + 1)
"
