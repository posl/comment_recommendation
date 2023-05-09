def get_key(s):
    return [key.index(c) for c in s]
key = input()
N = int(input())
S = [input() for _ in range(N)]
for s in sorted(S, key=get_key):
    print(s)
import sys
from collections import defaultdict
from itertools import permutations

if __name__ == '__main__':
    get_key()