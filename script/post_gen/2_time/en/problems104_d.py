Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    MOD = 10**9 + 7
    A = S.count('A')
    B = S.count('B')
    C = S.count('C')
    Q = S.count('?')
    # 3^Q
    three_Q = pow(3, Q, MOD)
    # 3^Q - 1
    three_Q_minus_1 = (three_Q - 1) % MOD
    # 3^Q - 1 / 2
    three_Q_minus_1_div_2 = pow(three_Q_minus_1, MOD - 2, MOD)
    # 3^Q - 1 / 2 * A
    A_ = (three_Q_minus_1_div_2 * A) % MOD
    # 3^Q - 1 / 2 * B
    B_ = (three_Q_minus_1_div_2 * B) % MOD
    # 3^Q - 1 / 2 * C
    C_ = (three_Q_minus_1_div_2 * C) % MOD
    # 3^Q - 1 / 2 * A * B
    AB = (A_ * B_) % MOD
    # 3^Q - 1 / 2 * B * C
    BC = (B_ * C_) % MOD
    # 3^Q - 1 / 2 * C * A
    CA = (C_ * A_) % MOD
    # 3^Q - 1 / 2 * A * B * C
    ABC = (AB * C_) % MOD
    # 3^Q - 1 / 2 * A + 3^Q - 1 / 2 * B + 3^Q - 1 / 2 * C - 3^Q - 1 / 2 * A * B - 3^Q - 1 / 2 * B * C - 3^Q - 1 / 2 * C * A + 3^Q - 1 / 2 * A * B * C
    print((A_ + B_ + C_ - AB - BC - CA + ABC) % MOD)

=======
Suggestion 2

def main():
    S = input()
    N = len(S)
    MOD = 10 ** 9 + 7
    dp = [[[0] * 4 for _ in range(4)] for _ in range(N + 1)]
    dp[0][3][3] = 1
    for i in range(N):
        for j in range(4):
            for k in range(4):
                if S[i] == '?':
                    for c in range(3):
                        dp[i + 1][j][c] += dp[i][j][k]
                        dp[i + 1][j][c] %= MOD
                else:
                    dp[i + 1][j][ord(S[i]) - ord('A')] += dp[i][j][k]
                    dp[i + 1][j][ord(S[i]) - ord('A')] %= MOD
        for j in range(4):
            for k in range(4):
                dp[i + 1][j][k] += dp[i][j][k]
                dp[i + 1][j][k] %= MOD
    ans = 0
    for j in range(4):
        for k in range(4):
            ans += dp[N][j][k]
            ans %= MOD
    print(ans)

=======
Suggestion 3

def main():
    S = input()
    N = len(S)
    MOD = 10**9 + 7
    dp = [[[0] * 4 for _ in range(4)] for _ in range(N + 1)]
    dp[0][0][0] = 1
    for i in range(N):
        if S[i] == "?":
            for j in range(4):
                for k in range(4):
                    for l in range(1, 4):
                        dp[i + 1][j][l] += dp[i][j][k]
                        dp[i + 1][j][l] %= MOD
                        dp[i + 1][k][l] += dp[i][j][k]
                        dp[i + 1][k][l] %= MOD
        else:
            for j in range(4):
                for k in range(4):
                    l = "ABC".index(S[i]) + 1
                    dp[i + 1][j][l] += dp[i][j][k]
                    dp[i + 1][j][l] %= MOD
                    dp[i + 1][k][l] += dp[i][j][k]
                    dp[i + 1][k][l] %= MOD
    ans = 0
    for j in range(4):
        for k in range(4):
            ans += dp[N][j][k]
            ans %= MOD
    print(ans)

=======
Suggestion 4

def main():
    S = input()
    N = len(S)
    MOD = 10**9 + 7
    dp = [[[0] * 4 for _ in range(4)] for _ in range(N+1)]
    dp[0][0][0] = 1
    for i in range(N):
        for j in range(4):
            for k in range(4):
                if S[i] == "?":
                    for l in range(3):
                        dp[i+1][j][k] += dp[i][j][k]
                        dp[i+1][j][k] %= MOD
                        dp[i+1][l][j] += dp[i][j][k]
                        dp[i+1][l][j] %= MOD
                else:
                    dp[i+1][j][k] += dp[i][j][k]
                    dp[i+1][j][k] %= MOD
                    dp[i+1][ord(S[i])-ord("A")][j] += dp[i][j][k]
                    dp[i+1][ord(S[i])-ord("A")][j] %= MOD
    ans = 0
    for j in range(4):
        for k in range(4):
            ans += dp[N][j][k]
            ans %= MOD
    print(ans)

=======
Suggestion 5

def main():
    S = input()
    MOD = 10**9 + 7
    N = len(S)
    dp = [[[0]*3 for _ in range(3)] for _ in range(N+1)]
    dp[0][0][0] = 1
    for i in range(N):
        for j in range(3):
            for k in range(3):
                if S[i] == "?":
                    for l in range(3):
                        dp[i+1][(j+l)%3][(k+l)%3] += dp[i][j][k]
                        dp[i+1][(j+l)%3][(k+l)%3] %= MOD
                else:
                    l = ord(S[i]) - ord("A")
                    dp[i+1][(j+l)%3][(k+l)%3] += dp[i][j][k]
                    dp[i+1][(j+l)%3][(k+l)%3] %= MOD
    print(dp[N][0][0])

=======
Suggestion 6

def main():
    MOD = 10**9 + 7
    s = input()
    n = len(s)
    dp = [[[0] * 3 for _ in range(3)] for _ in range(n + 1)]
    dp[0][0][0] = 1
    for i in range(n):
        for j in range(3):
            for k in range(3):
                if s[i] == "?":
                    for l in range(3):
                        dp[i + 1][j][k] += dp[i][j][k]
                        if j == 0 and k == 1:
                            dp[i + 1][j][k] += dp[i][j][k]
                        if j == 0 and k == 2:
                            dp[i + 1][j][k] += dp[i][j][k]
                        if j == 1 and k == 2:
                            dp[i + 1][j][k] += dp[i][j][k]
                        if j == 1 and k == 0:
                            dp[i + 1][j][k] += dp[i][j][k]
                        if j == 2 and k == 0:
                            dp[i + 1][j][k] += dp[i][j][k]
                        if j == 2 and k == 1:
                            dp[i + 1][j][k] += dp[i][j][k]
                        dp[i + 1][j][k] %= MOD
                else:
                    dp[i + 1][j][k] += dp[i][j][k]
                    if j == 0 and k == 1 and s[i] == "C":
                        dp[i + 1][j][k] += dp[i][j][k]
                    if j == 0 and k == 2 and s[i] == "B":
                        dp[i + 1][j][k] += dp[i][j][k]
                    if j == 1 and k == 2 and s[i] == "A":
                        dp[i + 1][j][k] += dp[i][j][k]
                    if j == 1 and k == 0 and s[i] == "C":
                        dp[i + 1][j][k] += dp[i][j][k]
                    if j == 2

=======
Suggestion 7

def main():
    s = input()
    mod = 10 ** 9 + 7
    abc = [0, 0, 0]
    ans = 1
    for c in s:
        if c == '?':
            ans *= 3
            ans %= mod
            abc = [abc[0] * 3 + abc[1], abc[0] + abc[1] * 3 + abc[2], abc[1] + abc[2] * 3]
            abc[0] %= mod
            abc[1] %= mod
            abc[2] %= mod
        else:
            abc = [abc[0] * (c == 'A') + abc[1] * (c == 'B'), abc[0] * (c == 'B') + abc[1] * (c == 'C') + abc[2] * (c == 'A'), abc[1] * (c == 'A') + abc[2] * (c == 'B')]
    print((abc[2] * ans) % mod)

=======
Suggestion 8

def main():
    S = input()
    mod = 10**9+7
    N = len(S)
    dp = [[0]*4 for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(4):
            if S[i] == "?":
                dp[i+1][j] = dp[i][j]*3
            else:
                dp[i+1][j] = dp[i][j]
        if S[i] == "A" or S[i] == "?":
            dp[i+1][1] += dp[i][0]
        if S[i] == "B" or S[i] == "?":
            dp[i+1][2] += dp[i][1]
        if S[i] == "C" or S[i] == "?":
            dp[i+1][3] += dp[i][2]
        for j in range(4):
            dp[i+1][j] %= mod
    print(dp[N][3])

=======
Suggestion 9

def main():
    S = input()
    mod = 10**9 + 7
    N = len(S)
    ans = 0
    for i in range(N):
        if S[i] == "A":
            for j in range(i+1, N):
                if S[j] == "B":
                    for k in range(j+1, N):
                        if S[k] == "C":
                            ans += 1
    print(ans % mod)

=======
Suggestion 10

def main():
    from sys import stdin
    from collections import Counter
    from itertools import product
    from functools import reduce
    from operator import mul
    from math import factorial
    from math import log10
    from math import pow
    from math import floor
    from math import ceil
    from math import gcd
    from math import sqrt
    from math import pi
    from math import inf
    from math import e
    from bisect import bisect_left
    from bisect import bisect_right
    from bisect import insort_left
    from bisect import insort_right
    from heapq import heappush
    from heapq import heappop
    from heapq import heapify
    from heapq import heappushpop
    from heapq import heapreplace
    from heapq import merge
    from random import randint
    from random import shuffle
    from random import sample
    from random import choice
    from random import choices
    from random import randrange
    from random import random
    from random import triangular
    from random import uniform
    from random import gauss
    from random import betavariate
    from random import expovariate
    from random import gammavariate
    from random import lognormvariate
    from random import normalvariate
    from random import vonmisesvariate
    from random import paretovariate
    from random import weibullvariate
    from decimal import Decimal
    from decimal import getcontext
    from decimal import ROUND_CEILING
    from decimal import ROUND_DOWN
    from decimal import ROUND_FLOOR
    from decimal import ROUND_HALF_DOWN
    from decimal import ROUND_HALF_EVEN
    from decimal import ROUND_HALF_UP
    from decimal import ROUND_UP
    from decimal import ROUND_05UP
    from typing import Any
    from typing import Union
    from typing import NoReturn
    from typing import Optional
    from typing import List
    from typing import Tuple
    from typing import Callable
    from typing import Iterable
    from typing import Iterator
    from typing import Sequence
    from typing import Mapping
    from typing import MutableSequence
    from typing import MutableMapping
    from typing import Counter as CounterType
    from typing import Set
    from typing import MutableSet
    from typing import Dict
    from typing import DefaultDict
    from
