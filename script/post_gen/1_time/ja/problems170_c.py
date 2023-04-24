Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    X, N = map(int, input().split())
    if N == 0:
        print(X)
    else:
        p = list(map(int, input().split()))
        if X not in p:
            print(X)
        else:
            for i in range(101):
                if (X - i) not in p:
                    print(X - i)
                    break
                elif (X + i) not in p:
                    print(X + i)
                    break

=======
Suggestion 2

def main():
    x, n = map(int, input().split())
    if n == 0:
        print(x)
        return
    p = list(map(int, input().split()))
    p.sort()
    if x < p[0]:
        print(p[0])
        return
    if x > p[-1]:
        print(p[-1])
        return
    for i in range(n):
        if p[i] == x:
            print(p[i+1])
            return
        if p[i+1] > x:
            if p[i+1] - x < x - p[i]:
                print(p[i+1])
                return
            else:
                print(p[i])
                return

=======
Suggestion 3

def main():
    X, N = map(int, input().split())
    if N == 0:
        print(X)
        return
    p = list(map(int, input().split()))
    p.sort()
    if X <= p[0]:
        print(p[0])
        return
    if X >= p[-1]:
        print(p[-1])
        return
    for i in range(N-1):
        if p[i] < X and X < p[i+1]:
            if (X-p[i]) <= (p[i+1]-X):
                print(p[i])
                return
            else:
                print(p[i+1])
                return

=======
Suggestion 4

def main():
    X, N = map(int, input().split())
    p = list(map(int, input().split())) if N > 0 else []
    for i in range(100):
        if X - i not in p:
            print(X - i)
            return
        if X + i not in p:
            print(X + i)
            return

=======
Suggestion 5

def main():
    X, N = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    for i in range(101):
        if (X - i) not in p:
            print(X - i)
            return
        if (X + i) not in p:
            print(X + i)
            return

=======
Suggestion 6

def main():
    X, N = map(int, input().split())
    if N == 0:
        print(X)
    else:
        P = list(map(int, input().split()))
        #print(X, N, P)
        for i in range(101):
            if X-i not in P:
                print(X-i)
                break
            elif X+i not in P:
                print(X+i)
                break

=======
Suggestion 7

def main():
    x = int(input().split()[0])
    p = set(map(int, input().split()))
    for i in range(1000):
        if x - i not in p:
            print(x - i)
            return
        if x + i not in p:
            print(x + i)
            return

=======
Suggestion 8

def main():
    x, n = map(int,input().split())
    if n == 0:
        print(x)
        return
    p = list(map(int,input().split()))
    p.sort()
    for i in range(100):
        if x - i not in p:
            print(x - i)
            return
        if x + i not in p:
            print(x + i)
            return

=======
Suggestion 9

def main():
    x, n = map(int, input().split())
    if n == 0:
        print(x)
        exit()
    p = list(map(int, input().split()))
    p.sort()
    p.append(1000)
    ans = 1000
    for i in range(1, n + 1):
        if p[i] - p[i - 1] > 1:
            for j in range(p[i - 1] + 1, p[i]):
                if abs(x - j) < abs(x - ans):
                    ans = j
    print(ans)

=======
Suggestion 10

def main():
    X, N = map(int, input().split())
    p = list(map(int, input().split()))
    
    ans = X
    for i in range(101):
        if (X - i) not in p:
            ans = X - i
            break
        elif (X + i) not in p:
            ans = X + i
            break
    
    print(ans)
