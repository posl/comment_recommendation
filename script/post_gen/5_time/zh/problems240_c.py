Synthesizing 10/10 solutions

=======
Suggestion 1

def can_jump(x, jump):
    if x == 0:
        return True
    if jump == []:
        return False
    return can_jump(x-jump[0], jump[1:]) or can_jump(x+jump[0], jump[1:])

=======
Suggestion 2

def check(X, N, a, b):
    if X == 0:
        return True
    elif N == 0:
        return False
    else:
        return check(X - a[N-1], N-1, a, b) or check(X - b[N-1], N-1, a, b)

=======
Suggestion 3

def jump(N, X, a, b):
    # 从第N个开始跳，看是否能跳到X
    if N == 0:
        return False
    if X == a[N - 1] or X == b[N - 1]:
        return True
    if X < a[N - 1]:
        return False
    if X > b[N - 1]:
        return False
    return jump(N - 1, X - a[N - 1], a, b) or jump(N - 1, X - b[N - 1], a, b)

=======
Suggestion 4

def solve():
    N, X = map(int, input().split())
    a = []
    b = []
    for i in range(N):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    # print(a)
    # print(b)
    # print(X)
    sum = 0
    for i in range(N):
        if (i+1) % 2 == 0:
            sum += b[i]
        else:
            sum += a[i]
    if sum >= X:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def jumpable(n, x, a, b):
    if x == 0:
        return True
    if n == 0:
        return False
    if jumpable(n-1, x-a[n-1], a, b) or jumpable(n-1, x-b[n-1], a, b):
        return True
    return False

=======
Suggestion 6

def main():
    n, x = map(int, input().split())
    for i in range(n):
        a, b = map(int, input().split())
        if (x - a) % b == 0:
            print('Yes')
            return
    print('No')

=======
Suggestion 7

def jump(n, x, a, b):
    current = 0
    for i in range(n):
        if (x - current) % a[i] == 0:
            return 'Yes'
        elif (x - current) % b[i] == 0:
            return 'Yes'
        else:
            current += a[i]
    return 'No'

=======
Suggestion 8

def canReach(X, N, a, b):
    # 从第N次开始跳
    if X == 0:
        return True
    if N == 0:
        return False
    if X < 0:
        return False
    return canReach(X - a[N - 1], N - 1, a, b) or canReach(X - b[N - 1], N - 1, a, b)

N, X = map(int, input().split())
a = []
b = []
for i in range(N):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)

=======
Suggestion 9

def main():
    n, x = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[1], reverse=True)
    for a, b in ab:
        if x == a or x == b:
            print('Yes')
            break
        elif x > a:
            x -= a
            x += b
        else:
            print('No')
            break
    else:
        print('No')

=======
Suggestion 10

def jump(n, x, a, b):
    if x == 0:
        return True
    if n == 0:
        return False
    return jump(n - 1, x - a[n - 1], a, b) or jump(n - 1, x - b[n - 1], a, b)
