def main():
    import sys
    import math
    #from collections import defaultdict
    #from collections import deque
    #import heapq
    #from fractions import gcd
    #from collections import Counter
    #from itertools import combinations
    
    #input = sys.stdin.readline
    
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    
    print(math.ceil(N/min(A,B,C,D,E))+4)
