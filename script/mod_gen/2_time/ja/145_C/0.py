def dist(a,b):
    return ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5
N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
import itertools
import numpy as np
ans = 0
for p in itertools.permutations(range(N)):
    for i in range(N-1):
        ans += dist(XY[p[i]],XY[p[i+1]])
ans /= np.math.factorial(N)
print(ans)
from itertools import permutations
from math import sqrt

if __name__ == '__main__':
    dist()