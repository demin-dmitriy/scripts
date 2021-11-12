#!/usr/bin/env bash
    # --matplotlib=tk \
exec ipython3 \
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
import functools; from functools import reduce, partial, partialmethod, singledispatch
import collections; from collections import *
import pickle

# System
import json
import sys
import os
import time; from time import sleep
from pathlib import Path

HOME = Path('~').expanduser()

segment = lambda a, b: range(a, b + 1)
"