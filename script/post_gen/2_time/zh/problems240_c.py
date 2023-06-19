Synthesizing 10/10 solutions

=======
Suggestion 1

def jump(n,x,ab):
    if n == 0:
        return False
    if n == 1:
        if x == ab[0][0] or x == ab[0][1]:
            return True
        else:
            return False
    if n > 1:
        for i in range(n):
            if x == ab[i][0] or x == ab[i][1]:
                return True
            else:
                return jump(n-1,x-ab[i][0],ab) or jump(n-1,x-ab[i][1],ab)
    return False
n,x = map(int,input().split())
ab = []
for i in range(n):
    ab.append(list(map(int,input().split())))

=======
Suggestion 2

def solve():
    N, X = map(int, input().split())
    a = []
    b = []
    for i in range(N):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)

    cur = 0
    for i in range(N):
        cur += a[i]
        if cur > X:
            print("No")
            return
        cur += b[i] - a[i]
    if cur == X:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def solve():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    d = [0] * (x + 1)
    d[0] = 1
    for i in range(n):
        for j in range(a[i], x + 1):
            if d[j - a[i]]:
                d[j] = 1
        for j in range(b[i], x + 1):
            if d[j - b[i]]:
                d[j] = 1
    if d[x]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def jump(i, x):
    if i >= N:
        return False
    if x == X:
        return True
    return jump(i + 1, x + a[i]) or jump(i + 1, x + b[i])

N, X = map(int, input().split())
a = []
b = []
for i in range(N):
    a_i, b_i = map(int, input().split())
    a.append(a_i)
    b.append(b_i)
print("Yes" if jump(0, 0) else "No")

=======
Suggestion 5

def jump(jumps, x):
    if jumps[0][1] >= x:
        return 'Yes'
    for i in range(1, len(jumps)):
        if jumps[i][0] >= jumps[i-1][1] and jumps[i][1] >= x:
            return 'Yes'
    return 'No'

=======
Suggestion 6

def solve():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)

    dp = [[False] * (x + 1) for _ in range(n + 1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(x + 1):
            if dp[i][j]:
                dp[i + 1][j + a[i]] = True
                dp[i + 1][j + b[i]] = True

    print("Yes" if dp[n][x] else "No")

=======
Suggestion 7

def main():
    n,x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    print(a)
    print(b)

    sum = 0
    for i in range(n):
        sum += a[i]
        if sum > x:
            print("No")
            return
        sum += b[i]
    if sum == x:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    n, x = map(int, input().split())
    for i in range(n):
        a, b = map(int, input().split())
        if (b - a) <= x:
            pass
        else:
            print('No')
            return
    print('Yes')

=======
Suggestion 9

def main():
    N,X = map(int,input().split())
    a = [0 for i in range(N)]
    b = [0 for i in range(N)]
    for i in range(N):
        a[i],b[i] = map(int,input().split())
    for i in range(N):
        if X == a[i] or X == b[i]:
            print("Yes")
            return
    print("No")

=======
Suggestion 10

def main():
    n,x = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        ta,tb = map(int,input().split())
        a.append(ta)
        b.append(tb)
    pos = 0
    for i in range(n):
        if (pos + a[i]) > x:
            print("No")
            return
        else:
            pos += b[i] - a[i]
    if pos == x:
        print("Yes")
    else:
        print("No")
