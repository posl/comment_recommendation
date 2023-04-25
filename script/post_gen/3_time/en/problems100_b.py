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
    else:
        if N == 100:
            print(1010000)
        else:
            print(N * 10000)

main()

=======
Suggestion 2

def main():
    d, n = map(int, input().split())
    if d == 0:
        print(n)
    elif d == 1:
        if n == 100:
            print(10100)
        else:
            print(n*100)
    else:
        if n == 100:
            print(1010000)
        else:
            print(n*10000)

=======
Suggestion 3

def main():
    D, N = map(int, input().split())
    if N != 100:
        print(N * 100 ** D)
    else:
        print((N + 1) * 100 ** D)

=======
Suggestion 4

def main():
    D, N = map(int, input().split())
    if N == 100:
        N += 1
    print(N * 100 ** D)

=======
Suggestion 5

def main():
    d, n = map(int, input().split())
    if n == 100:
        n += 1
    print(n * 100 ** d)

=======
Suggestion 6

def main():
    d, n = map(int, input().split())
    if n == 100:
        n += 1
    print(n * (100 ** d))

=======
Suggestion 7

def getInteger(D, N):
    if D == 0:
        return N
    elif D == 1:
        return N * 100
    elif D == 2:
        return N * 10000

D, N = map(int, input().split())
print(getInteger(D, N))

=======
Suggestion 8

def main():
    D, N = (int(x) for x in input().split())
    if N == 100:
        N += 1
    print(N * 100 ** D)

=======
Suggestion 9

def main():
    D, N = map(int, input().split())
    if N == 100:
        N = 101
    print(N*(100**D))
