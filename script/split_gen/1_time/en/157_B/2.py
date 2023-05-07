def bingo():
    A = [list(map(int, input().split())) for _ in range(3)]
    N = int(input())
    B = [int(input()) for _ in range(N)]
    for i in range(3):
        for j in range(3):
            if A[i][j] in B:
                A[i][j] = 0
    for i in range(3):
        if A[i][0] == A[i][1] == A[i][2] == 0:
            return "Yes"
        if A[0][i] == A[1][i] == A[2][i] == 0:
            return "Yes"
    if A[0][0] == A[1][1] == A[2][2] == 0:
        return "Yes"
    if A[0][2] == A[1][1] == A[2][0] == 0:
        return "Yes"
    return "No"
print(bingo())
import sys
import math
import itertools
import collections
import heapq
import queue
import bisect
import copy
import decimal
import string
import fractions
import random
import functools
import statistics
import re
import numpy as np
import scipy as sp
import scipy.sparse.csgraph
import scipy.sparse.csgraph._validation
import scipy.sparse.csgraph._shortest_path
import scipy.sparse.csgraph._tools
import scipy.sparse.csgraph._traversal
import scipy.sparse.csgraph._min_spanning_tree
import scipy.sparse.csgraph._reordering
import scipy.sparse.csgraph._laplacian
import scipy.sparse.csgraph._flow
import scipy.sparse.csgraph._matching
import scipy.sparse.csgraph._maxflow
import scipy.sparse.csgraph._min_cost_flow
import scipy.sparse.csgraph._construct
import scipy.sparse.csgraph._reordering
import scipy.sparse.csgraph._min_spanning_tree
import scipy.sparse.csgraph._traversal
import scipy.sparse.csgraph._validation
import scipy.sparse.csgraph._shortest_path
import scipy.sparse.csgraph._tools
import scipy.sparse.csgraph._laplacian
import scipy.sparse.csgraph._flow
import scipy.sparse.csgraph._matching
import scipy.sparse.csgraph._maxflow
import scipy.sparse.csgraph._min_cost_flow
import scipy.sparse.csgraph._construct
import scipy.sparse.csgraph._reordering
