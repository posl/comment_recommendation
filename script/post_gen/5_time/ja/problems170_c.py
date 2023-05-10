Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x, n = map(int, input().split())
    if n == 0:
        print(x)
        return
    p = list(map(int, input().split()))
    p.sort()
    for i in range(100):
        if x-i not in p:
            print(x-i)
            return
        if x+i not in p:
            print(x+i)
            return

=======
Suggestion 2

def main():
    x, n = map(int, input().split())
    p = set(map(int, input().split()))
    for i in range(100):
        if x-i not in p:
            print(x-i)
            return
        elif x+i not in p:
            print(x+i)
            return

=======
Suggestion 3

def main():
    X, N = map(int, input().split())
    if N == 0:
        print(X)
        return
    P = list(map(int, input().split()))
    for i in range(0, X+1):
        if X-i not in P:
            print(X-i)
            return
        if X+i not in P:
            print(X+i)
            return

=======
Suggestion 4

def main():
    X, N = map(int, input().split())
    if N == 0:
        print(X)
        return
    p = list(map(int, input().split()))
    p.sort()
    for i in range(1, X + 1):
        if not i in p:
            print(i)
            return
    for i in range(X, 0, -1):
        if not i in p:
            print(i)
            return

=======
Suggestion 5

def main():
    X, N = map(int, input().split())
    p = list(map(int, input().split()))
    if N == 0:
        print(X)
        exit()
    p = sorted(p)
    if X not in p:
        print(X)
        exit()
    for i in range(1, 100):
        if X - i not in p:
            print(X-i)
            exit()
        elif X + i not in p:
            print(X+i)
            exit()
    print(0)

=======
Suggestion 6

def main():
    x,n = map(int,input().split())
    if n == 0:
        print(x)
        return
    p = list(map(int,input().split()))
    if x not in p:
        print(x)
        return
    p.sort()
    for i in range(1,101):
        if x-i not in p:
            print(x-i)
            return
        elif x+i not in p:
            print(x+i)
            return

=======
Suggestion 7

def main():
    x, n = map(int, input().split())
    p = list(map(int, input().split()))
    for i in range(200):
        if x - i not in p:
            print(x - i)
            break
        elif x + i not in p:
            print(x + i)
            break

=======
Suggestion 8

def main():
    x,n = map(int,input().split())
    p = list(map(int,input().split()))
    ans = 0
    for i in range(x,101):
        if i not in p:
            ans = i
            break
    for i in range(x,0,-1):
        if i not in p:
            if ans == 0:
                ans = i
            else:
                if abs(x-i) <= abs(x-ans):
                    ans = i
                break
    print(ans)

=======
Suggestion 9

def main():
    X, N = map(int, input().split())
    if N == 0:
        print(X)
        return
    p = list(map(int, input().split()))
    p.sort()
    for i in range(0, 102):
        if (X - i) not in p:
            print(X - i)
            return
        if (X + i) not in p:
            print(X + i)
            return

=======
Suggestion 10

def main():
    x, n = map(int, input().split())
    p = list(map(int, input().split()))
    if n == 0:
        print(x)
        return
    min_diff = 1000
    min_num = 0
    for i in range(102):
        if i in p:
            continue
        diff = abs(x - i)
        if diff < min_diff:
            min_diff = diff
            min_num = i
    print(min_num)
