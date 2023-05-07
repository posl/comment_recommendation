def main():
    N, K = map(int, input().split())
    c = list(map(int, input().split()))
    # print(N, K, c)
    # print(c[0:K])
    # print(set(c[0:K]))
    # print(len(set(c[0:K])))
    ans = 0
    for i in range(N-K+1):
        ans = max(ans, len(set(c[i:i+K])))
    print(ans)
main()
import sys
import math
import copy
import collections
import itertools
import numpy as np
import pandas as pd
import scipy as sp
import scipy.stats

if __name__ == '__main__':
    main()