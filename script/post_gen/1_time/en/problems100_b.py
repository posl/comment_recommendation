Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    D, N = map(int, input().split())
    if N == 100:
        print(101*100**D)
    else:
        print(N*100**D)

=======
Suggestion 2

def main():
    D, N = map(int, input().split())
    if N == 100:
        N += 1
    print(N * 100 ** D)

=======
Suggestion 3

def main():
    D, N = map(int, input().split())
    if N == 100:
        N += 1
    print(N * 100**D)

main()

=======
Suggestion 4

def main():
    D, N = list(map(int, input().split()))
    if N == 100:
        print(101 * 100 ** D)
    else:
        print(N * 100 ** D)

=======
Suggestion 5

def get100s(d, n):
    if d == 0:
        return n
    elif d == 1:
        return n * 100
    elif d == 2:
        return n * 10000
    else:
        return 0

=======
Suggestion 6

def getNthSmallestDivisibleBy100(D,N):
    if D == 0:
        return N
    elif D == 1:
        return 100 * N
    elif D == 2:
        return 10000 * N

D,N = input().split()
D = int(D)
N = int(N)

=======
Suggestion 7

def main():
    D, N = map(int, input().split())
    print(100**D * (N + (N == 100)))

=======
Suggestion 8

def main():
    # Read the input
    D, N = list(map(int, input().split()))
    # Find the N-th smallest integer that can be divided by 100 exactly D times
    if N == 100:
        if D == 0:
            print(101)
        else:
            print(10100)
    else:
        if D == 0:
            print(N)
        elif D == 1:
            print(N*100)
        else:
            print(N*10000)
