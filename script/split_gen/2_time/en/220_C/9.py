def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    A_sum = sum(A)
    if A_sum > X:
        print('N')
        return
    B = A * 100000
    B_sum = sum(B)
    k = 0
    while X > B_sum:
        X -= A_sum
        k += N
    for i in range(N):
        X -= A[i]
        k += 1
        if X < 0:
            break
    print(k)
main()
import math
import sys
import itertools
import collections
from collections import deque
from collections import defaultdict
from collections import Counter
from fractions import gcd
import heapq
import bisect
import copy
import string
import re
import numpy as np
import scipy as sp
import scipy.sparse
import scipy.sparse.csgraph
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from io import StringIO
import time
import random
import queue
import sys
import math
import time
import datetime
import operator
from functools import reduce
from functools import lru_cache
from itertools import accumulate
from itertools import combinations
from itertools import combinations_with_replacement
from itertools import permutations
from itertools import product
from itertools import groupby
from bisect import bisect_left
from bisect import bisect_right
from bisect import insort_left
from bisect import insort_right
from operator import itemgetter
from operator import mul
from operator import add
from operator import sub
from operator import xor
from operator import truediv
from operator import floordiv
from operator import mod
from operator import pow
from operator import lt
from operator import le
from operator import eq
from operator import ne
from operator import ge
from operator import gt
from operator import iadd
from operator import isub
from operator import imul
from operator import itruediv
from operator import ifloordiv
from operator import imod
from operator import ipow
from operator import iand
from operator import ixor
from operator import ilshift
from operator import irshift
from operator import ior
from collections import deque
from collections import defaultdict
from collections import Counter
from collections import OrderedDict
from collections import namedtuple
from collections.
