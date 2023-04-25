Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    X, N = map(int, input().split())
    if N == 0:
        print(X)
        return
    p = set(map(int, input().split()))
    for i in range(101):
        if X - i not in p:
            print(X - i)
            return
        if X + i not in p:
            print(X + i)
            return

=======
Suggestion 2

def main():
    x, n = map(int, input().split())
    p = list(map(int, input().split()))
    if n == 0:
        print(x)
        return
    if x not in p:
        print(x)
        return
    for i in range(100):
        if x - i not in p:
            print(x - i)
            return
        if x + i not in p:
            print(x + i)
            return

=======
Suggestion 3

def main():
    X, N = map(int, input().split())
    p = list(map(int, input().split()))
    for i in range(100):
        if X - i not in p:
            print(X - i)
            break
        elif X + i not in p:
            print(X + i)
            break

=======
Suggestion 4

def main():
    X, N = map(int, input().split())
    p = list(map(int, input().split()))
    for i in range(1000):
        if X - i not in p:
            print(X - i)
            return
        if X + i not in p:
            print(X + i)
            return

=======
Suggestion 5

def find_nearest(X, p):
    if len(p) == 0:
        return X
    else:
        p.sort()
        if X < p[0]:
            return p[0]
        elif X > p[-1]:
            return p[-1]
        else:
            for i in range(len(p) - 1):
                if p[i] < X < p[i + 1]:
                    if X - p[i] <= p[i + 1] - X:
                        return p[i]
                    else:
                        return p[i + 1]

=======
Suggestion 6

def main():
    # Get the input
    x, n = map(int, input().split())
    if n == 0:
        print(x)
        return
    ps = set(map(int, input().split()))
    
    # Find the nearest integer
    for i in range(0, 100):
        if x - i not in ps:
            print(x - i)
            return
        if x + i not in ps:
            print(x + i)
            return

=======
Suggestion 7

def main():
    # 1. Input
    x, n = map(int, input().split())
    p = list(map(int, input().split()))
    # 2. Process
    if n == 0:
        ans = x
    else:
        p.sort()
        if x < p[0]:
            ans = p[0] - 1
        elif p[-1] < x:
            ans = p[-1] + 1
        else:
            for i in range(n - 1):
                if p[i] <= x and x <= p[i + 1]:
                    if x - p[i] < p[i + 1] - x:
                        ans = p[i]
                    elif x - p[i] > p[i + 1] - x:
                        ans = p[i + 1]
                    else:
                        ans = p[i]
                    break
    # 3. Output
    print(ans)

=======
Suggestion 8

def nearestXor(x, n, p):
    if n == 0:
        return x
    p = set(p)
    if x not in p:
        return x
    for i in range(1, 101):
        if x - i not in p:
            return x - i
        if x + i not in p:
            return x + i

=======
Suggestion 9

def get_nearest_number(x, n, p):
    if n == 0:
        return x
    else:
        # 1 <= p_i <= 100
        # 1 <= X <= 100
        # 0 <= N <= 100
        # so, 0 <= d <= 200
        d = 200
        for i in range(1, 101):
            if i not in p:
                if abs(x - i) < d:
                    d = abs(x - i)
                    nearest_number = i
        return nearest_number

=======
Suggestion 10

def nearest_integer(X, N, p):
    # Write your code here
    return 0
