Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    D, N = map(int, input().split())
    if D == 0:
        if N == 100:
            print(101)
        else:
            print(N)
    elif D == 1:
        if N == 100:
            print(10100)
        else:
            print(N * 100)
    elif D == 2:
        if N == 100:
            print(1010000)
        else:
            print(N * 10000)

=======
Suggestion 2

def main():
    D, N = map(int, input().split())
    if D == 0:
        if N == 100:
            print(101)
        else:
            print(N)
    elif D == 1:
        if N == 100:
            print(10100)
        else:
            print(N * 100)
    else:
        if N == 100:
            print(1010000)
        else:
            print(N * 10000)

=======
Suggestion 3

def main():
    D, N = map(int, input().split())
    if D == 0:
        if N == 100:
            print(101)
        else:
            print(N)
    elif D == 1:
        if N == 100:
            print(10100)
        else:
            print(N * 100)
    elif D == 2:
        if N == 100:
            print(1010000)
        else:
            print(N * 10000)

main()

=======
Suggestion 4

def main():
    d, n = map(int, input().split())
    if d == 0:
        if n == 100:
            print(101)
        else:
            print(n)
    elif d == 1:
        if n == 100:
            print(10100)
        else:
            print(n*100)
    elif d == 2:
        if n == 100:
            print(1010000)
        else:
            print(n*10000)

=======
Suggestion 5

def main():
    D, N = map(int, input().split())
    if N == 100:
        N += 1
    print(100 ** D * N)

=======
Suggestion 6

def main():
    d, n = map(int, input().split())
    if n != 100:
        print(100**d * n)
    else:
        print(100**d * n + 100**d)

=======
Suggestion 7

def main():
    D, N = map(int, input().split())
    if N == 100:
        N += 1
    print(N * 100 ** D)
