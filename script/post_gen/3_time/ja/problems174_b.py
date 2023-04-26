Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, d = map(int, input().split())
    count = 0
    for i in range(n):
        x, y = map(int, input().split())
        if x**2 + y**2 <= d**2:
            count += 1
    print(count)

=======
Suggestion 2

def main():
    N, D = map(int, input().split())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    count = 0
    for i in range(N):
        if (X[i]**2 + Y[i]**2) ** 0.5 <= D:
            count += 1
    print(count)

=======
Suggestion 3

def main():
    N, D = map(int, input().split())
    count = 0
    for i in range(N):
        X, Y = map(int, input().split())
        if (X**2 + Y**2)**(1/2) <= D:
            count += 1
    print(count)

=======
Suggestion 4

def main():
    N, D = map(int, input().split())
    ans = 0
    for i in range(N):
        X, Y = map(int, input().split())
        if X**2 + Y**2 <= D**2:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N, D = map(int, input().split())
    cnt = 0
    for i in range(N):
        X, Y = map(int, input().split())
        if (X**2 + Y**2) <= D**2:
            cnt += 1
    print(cnt)

=======
Suggestion 6

def main():
    N,D = map(int,input().split())
    X = []
    Y = []
    for i in range(N):
        x,y = map(int,input().split())
        X.append(x)
        Y.append(y)
    count = 0
    for i in range(N):
        if ((X[i]**2+Y[i]**2)**(1/2)) <= D:
            count += 1
    print(count)

=======
Suggestion 7

def main():
    N, D = map(int, input().split())
    ans = 0
    for i in range(N):
        x, y = map(int, input().split())
        if D >= (x**2+y**2)**(1/2):
            ans += 1
    print(ans)

=======
Suggestion 8

def get_input():
    n,d = map(int,input().split())
    xy = [list(map(int,input().split())) for _ in range(n)]
    return n,d,xy

=======
Suggestion 9

def solve():
    # coding: utf-8
    # Your code here!
    import math
    import sys
    input = sys.stdin.readline
    from collections import defaultdict
    from collections import deque
    
    n,d = map(int,input().split())
    ans = 0
    for i in range(n):
        x,y = map(int,input().split())
        if math.sqrt(x**2 + y**2) <= d:
            ans += 1
    print(ans)
