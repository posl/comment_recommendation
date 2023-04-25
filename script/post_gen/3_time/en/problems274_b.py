Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    X = [0] * W
    for j in range(W):
        for i in range(H):
            if C[i][j] == '#':
                X[j] += 1
    print(' '.join(map(str, X)))

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    X = [0] * W
    for i in range(H):
        for j in range(W):
            if C[i][j] == '#':
                X[j] += 1
    print(*X)

=======
Suggestion 3

def main():
    h, w = map(int, input().split())
    c = [input() for _ in range(h)]
    x = [0] * w
    for j in range(w):
        for i in range(h):
            if c[i][j] == '#':
                x[j] += 1
    print(' '.join(map(str, x)))

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    X = [0] * W
    for _ in range(H):
        for i, c in enumerate(input()):
            if c == '#':
                X[i] += 1
    print(*X)

=======
Suggestion 5

def main():
    h, w = map(int, input().split())
    c = [input() for _ in range(h)]
    for j in range(w):
        cnt = 0
        for i in range(h):
            if c[i][j] == '#':
                cnt += 1
        print(cnt, end=' ')
    print()

=======
Suggestion 6

def main():
    h, w = map(int, input().split())
    s = [input() for i in range(h)]
    for i in range(w):
        count = 0
        for j in range(h):
            if s[j][i] == '#':
                count += 1
        print(count, end=' ')
main()

from itertools import accumulate
h,w=map(int,input().split())
s=[input() for _ in range(h)]
for i in accumulate([s[j][i]=='#'for i in range(w)for j in range(h)]):
    if i%h==0:print(i//h,end=' ')

h, w = map(int, input().split())
s = [input() for i in range(h)]
for i in range(w):
    count = 0
    for j in range(h):
        if s[j][i] == '#':
            count += 1
    print(count, end=' ')

import sys
input = sys.stdin.readline

h, w = map(int, input().split())
s = [input() for _ in range(h)]
for i in range(w):
    print(sum(s[j][i] == '#' for j in range(h)), end=' ')

h, w = map(int, input().split())
s = [input() for i in range(h)]
for i in range(w):
    count = 0
    for j in range(h):
        if s[j][i] == '#':
            count += 1
    print(count, end=' ')

h, w = map(int, input().split())
s = [input() for i in range(h)]
for i in range(w):
    count = 0
    for j in range(h):
        if s[j][i] == '#':
            count += 1
    print(count, end=' ')

h, w = map(int, input().split())
s = [input() for i in range(h)]
for i in range(w):
    count = 0
    for j in range(h):
        if s[j][i] == '#':
            count += 1
    print(count, end=' ')

h, w = map(int, input().split())
s = [input() for i in range(h)]
for i in range(w):
    count = 0
    for j in range(h):
        if s[j][i] == '#':
            count +=

=======
Suggestion 7

def main():
    h, w = map(int, input().split())
    c = []
    for _ in range(h):
        c.append(input())
    ans = [0] * w
    for i in range(w):
        for j in range(h):
            if c[j][i] == "#":
                ans[i] += 1
    print(*ans)

=======
Suggestion 8

def main():
    # H, W
    HW = list(map(int, input().split()))
    # C_{i, j}
    C = []
    for i in range(HW[0]):
        C.append(list(input()))
    # X_j
    X = [0] * HW[1]
    for j in range(HW[1]):
        for i in range(HW[0]):
            if C[i][j] == '#':
                X[j] += 1
    # Output
    print(' '.join(map(str, X)))

=======
Suggestion 9

def main():
    # read H and W
    H, W = map(int, input().split())
    # read C
    C = []
    for i in range(H):
        C.append(input())
    # count boxes in each column
    X = [0] * W
    for j in range(W):
        for i in range(H):
            if C[i][j] == '#':
                X[j] += 1
    # print X
    for x in X:
        print(x, end=' ')
    print()

=======
Suggestion 10

def read_ints():
    return [int(x) for x in input().split()]
