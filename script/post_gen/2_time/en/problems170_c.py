Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    X, N = map(int, input().split())
    p = set(map(int, input().split()))
    if N == 0:
        print(X)
    else:
        for i in range(0, 101):
            if X - i not in p:
                print(X - i)
                break
            elif X + i not in p:
                print(X + i)
                break

=======
Suggestion 2

def main():
    X, N = map(int, input().split())
    if N == 0:
        print(X)
        return
    p = list(map(int, input().split()))
    p.sort()
    if X < p[0]:
        print(p[0])
        return
    if X > p[-1]:
        print(p[-1])
        return
    for i in range(N-1):
        if p[i] < X and X < p[i+1]:
            if X-p[i] <= p[i+1]-X:
                print(p[i])
                return
            else:
                print(p[i+1])
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
    elif p[-1] <= X:
        print(p[-1])
        return
    for i in range(1, N):
        if p[i - 1] < X and X < p[i]:
            if X - p[i - 1] <= p[i] - X:
                print(p[i - 1])
            else:
                print(p[i])
            return

main()

=======
Suggestion 4

def main():
    X, N = map(int, input().split())
    p = set(map(int, input().split()))
    for i in range(101):
        if not X - i in p:
            print(X - i)
            break
        if not X + i in p:
            print(X + i)
            break

=======
Suggestion 5

def main():
    X, N = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    if N == 0:
        print(X)
    else:
        i = 0
        while i < N:
            if X - p[i] < 0:
                break
            i += 1
        if i == 0:
            print(p[0])
        elif i == N:
            print(p[N-1])
        else:
            if p[i] - X < X - p[i-1]:
                print(p[i])
            elif p[i] - X > X - p[i-1]:
                print(p[i-1])
            else:
                print(p[i-1])

=======
Suggestion 6

def main():
    x, n, *p = map(int, open(0).read().split())
    if n == 0:
        print(x)
        return
    p = set(p)
    for d in range(101):
        if x - d not in p:
            print(x - d)
            return
        if x + d not in p:
            print(x + d)
            return
main()

=======
Suggestion 7

def main():
    X, N = [int(s) for s in input().split()]
    p = [int(s) for s in input().split()]
    if N == 0:
        print(X)
        return
    for i in range(101):
        if X - i not in p:
            print(X - i)
            return
        elif X + i not in p:
            print(X + i)
            return

main()

=======
Suggestion 8

def main():
    x, n = map(int, input().split())
    p = list(map(int, input().split()))
    if n == 0:
        print(x)
        return
    if n == 1:
        if x < p[0]:
            print(x + 1)
            return
        elif x > p[0]:
            print(x - 1)
            return
        else:
            print(x + 1)
            return
    p.sort()
    if x < p[0]:
        print(x)
        return
    if x > p[n - 1]:
        print(x)
        return
    for i in range(n - 1):
        if p[i] < x and x < p[i + 1]:
            if x - p[i] < p[i + 1] - x:
                print(p[i])
                return
            elif x - p[i] > p[i + 1] - x:
                print(p[i + 1])
                return
            else:
                print(p[i])
                return

=======
Suggestion 9

def main():
    X, N = map(int, input().split())
    p = list(map(int, input().split()))
    if N == 0:
        print(X)
        return
    p.sort()
    #print(p)
    if X <= p[0]:
        print(p[0])
        return
    if X >= p[-1]:
        print(p[-1] + 1)
        return
    for i in range(len(p) - 1):
        if p[i] < X and p[i + 1] > X:
            if X - p[i] == p[i + 1] - X:
                print(p[i])
                return
            if X - p[i] < p[i + 1] - X:
                print(p[i])
                return
            else:
                print(p[i + 1])
                return

main()

=======
Suggestion 10

def  main():
    x, n = [int(i) for i in input().split()]
    p = [int(i) for i in input().split()]
    for i in range(101):
        if x - i not in p:
            print(x - i)
            return
        if x + i not in p:
            print(x + i)
            return
