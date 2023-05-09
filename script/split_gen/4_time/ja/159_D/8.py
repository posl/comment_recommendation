def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
import math
N = int(input())
A = list(map(int, input().split(" ")))
