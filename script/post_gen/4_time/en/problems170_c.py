Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x, n = map(int, input().split())
    p = list(map(int, input().split()))
    if n == 0:
        print(x)
    else:
        for i in range(100):
            if x - i not in p:
                print(x - i)
                break
            elif x + i not in p:
                print(x + i)
                break

=======
Suggestion 2

def main():
    x,n = map(int,input().split())
    if n == 0:
        print(x)
        return
    p = list(map(int,input().split()))
    p.sort()
    if x not in p:
        print(x)
        return
    else:
        for i in range(101):
            if x - i not in p:
                print(x - i)
                return
            elif x + i not in p:
                print(x + i)
                return

=======
Suggestion 3

def main():
    x,n = map(int, input().split())
    if n == 0:
        print(x)
        return
    p = list(map(int, input().split()))
    p.sort()
    if x not in p:
        print(x)
        return
    for i in range(1,100):
        if x-i not in p:
            print(x-i)
            return
        if x+i not in p:
            print(x+i)
            return

=======
Suggestion 4

def main():
    X, N = map(int, input().split())
    if N == 0:
        print(X)
    else:
        p = list(map(int, input().split()))
        p.sort()
        for i in range(0, 101):
            if X - i not in p:
                print(X - i)
                break
            elif X + i not in p:
                print(X + i)
                break

=======
Suggestion 5

def main():
    x, n = map(int, input().split())
    p = list(map(int, input().split()))
    if n == 0:
        print(x)
        return
    p.sort()
    for i in range(0, 100):
        if not x - i in p:
            print(x - i)
            return
        if not x + i in p:
            print(x + i)
            return

=======
Suggestion 6

def main():
    x, n = map(int, input().split())
    p = list(map(int, input().split()))
    if n == 0:
        print(x)
        return
    p.sort()
    for i in range(100):
        if x - i not in p:
            print(x - i)
            return
        if x + i not in p:
            print(x + i)
            return

=======
Suggestion 7

def main():
    x, n = map(int, input().split())
    p = list(map(int, input().split()))
    if n == 0:
        print(x)
        exit()
    for i in range(1, 100):
        if x - i not in p:
            print(x-i)
            exit()
        elif x + i not in p:
            print(x+i)
            exit()

=======
Suggestion 8

def main():
    x, n = map(int, input().split())
    p = list(map(int, input().split()))
    p = set(p)
    for i in range(100):
        if x - i not in p:
            print(x - i)
            break
        if x + i not in p:
            print(x + i)
            break

=======
Suggestion 9

def main():
    # input
    X, N = map(int, input().split())
    p = list(map(int, input().split()))
    # compute

    # output
    print(solve(X, N, p))

=======
Suggestion 10

def solve(x, n, p):
    if n == 0:
        return x
    if x not in p:
        return x
    else:
        for i in range(1, 100):
            if x - i not in p:
                return x - i
            elif x + i not in p:
                return x + i
