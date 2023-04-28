Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    ans = 0
    for i in range(len(s)):
        ans += (ord(s[i]) - 64) * 26 ** (len(s) - i - 1)
    print(ans)

=======
Suggestion 2

def base26(s):
    res = 0
    for i in s:
        res = res * 26 + (ord(i) - ord('A') + 1)
    return res

=======
Suggestion 3

def main():
    S = input()
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ans = 0
    for i in range(len(S)):
        ans += alpha.index(S[i]) * (26 ** (len(S) - i - 1))
    print(ans + 1)

=======
Suggestion 4

def main():
    inp = input()
    l = len(inp)
    ans = 0
    for i in range(l):
        ans += (ord(inp[i]) - 64) * (26 ** (l - 1 - i))
    print(ans)

=======
Suggestion 5

def main():
    S = input()
    #print(S)
    #print(ord(S[0]) - ord('A'))
    #print(ord(S[1]) - ord('A'))
    #print(ord(S[2]) - ord('A'))
    #print(ord(S[3]) - ord('A'))
    #print(ord(S[4]) - ord('A'))
    #print(ord(S[5]) - ord('A'))
    #print(ord(S[6]) - ord('A'))
    #print(ord(S[7]) - ord('A'))
    #print(ord(S[8]) - ord('A'))
    #print(ord(S[9]) - ord('A'))
    #print(ord(S[10]) - ord('A'))
    #print(ord(S[11]) - ord('A'))
    #print(ord(S[12]) - ord('A'))
    #print(ord(S[13]) - ord('A'))
    #print(ord(S[14]) - ord('A'))
    #print(ord(S[15]) - ord('A'))
    #print(ord(S[16]) - ord('A'))
    #print(ord(S[17]) - ord('A'))
    #print(ord(S[18]) - ord('A'))
    #print(ord(S[19]) - ord('A'))
    #print(ord(S[20]) - ord('A'))
    #print(ord(S[21]) - ord('A'))
    #print(ord(S[22]) - ord('A'))
    #print(ord(S[23]) - ord('A'))
    #print(ord(S[24]) - ord('A'))
    #print(ord(S[25]) - ord('A'))
    #print(ord(S[26]) - ord('A'))
    #print(ord(S[27]) - ord('A'))
    #print(ord(S[28]) - ord('A'))
    #print(ord(S[29]) - ord('A'))
    #print(ord(S[30]) - ord('A'))
    #print(ord(S[31]) - ord('A'))
    #print(ord(S[32]) - ord('A'))
    #print(ord(S[33]) - ord('A'))
    #print(ord(S[34]) - ord('A'))
    #print(ord(S[35]) - ord('A'))
    #print(ord(S[36]) - ord('A'))
    #print(ord(S[37

=======
Suggestion 6

def problem285_c():
    S = input()
    l = len(S)
    ans = 0
    for i in range(l):
        ans += (ord(S[i])-ord('A')+1)*26**(l-i-1)
    print(ans)

=======
Suggestion 7

def get_problem_number(problem_id):
    problem_number = 0
    problem_id = problem_id[::-1]
    for i in range(len(problem_id)):
        problem_number += (ord(problem_id[i]) - 64) * (26**i)
    return problem_number

=======
Suggestion 8

def solution():
    s = input()
    order = 0
    for i in range(len(s)):
        order = order * 26 + (ord(s[i]) - ord('A') + 1)
    print(order)

solution()

=======
Suggestion 9

def main():
    import string
    import math
    #from collections import defaultdict, Counter
    #from itertools import product, combinations, permutations
    #from bisect import bisect_left, bisect_right
    #from heapq import heappop, heappush, heapify
    #from copy import deepcopy
    #from fractions import gcd
    #from functools import reduce
    #from operator import mul
    #from pprint import pprint

    # mod = 10**9+7
    # inf = float('inf')
    # n = int(input())
    # a,b,c = map(int, input().split())
    # s = input()
    # t = input()
    # a = list(map(int, input().split()))
    # a = [input() for i in range(n)]
    # a = [[int(i) for i in input().split()] for i in range(n)]
    # a = [int(input()) for i in range(n)]
    # a = [list(map(int, input().split())) for i in range(n)]

=======
Suggestion 10

def main():
    S = input()
    print(int(S, 36))
