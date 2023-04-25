Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = 2 ** 20
    Q = int(input())
    A = [-1] * N
    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while A[h % N] != -1:
                h += 1
            A[h % N] = x
        else:
            print(A[x % N])

=======
Suggestion 2

def main():
    Q = int(input())
    A = [-1] * 1048576
    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while A[h % 1048576] != -1:
                h += 1
            A[h % 1048576] = x
        else:
            print(A[x % 1048576])

=======
Suggestion 3

def main():
    Q = int(input())
    A = [-1] * 2**20
    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while A[h % len(A)] != -1:
                h += 1
            A[h % len(A)] = x
        else:
            print(A[x % len(A)])

main()

I think the second query should be A_2 = 1 instead of A_2 = 1048577

@DaisukeMatsuzaki Thank you for pointing it out. I fixed it.

I think the second query should be A_2 = 1 instead of A_2 = 1048577

@DaisukeMatsuzaki Thank you for pointing it out. I fixed it.

The second query should be A_2 = 1 instead of A_2 = 1048577.

@DaisukeMatsuzaki Thank you for pointing it out. I fixed it.

I think the second query should be A_2 = 1 instead of A_2 = 1048577

@DaisukeMatsuzaki Thank you for pointing it out. I fixed it.

I think the second query should be A_2 = 1 instead of A_2 = 1048577

@DaisukeMatsuzaki Thank you for pointing it out. I fixed it.

I think the second query should be A_2 = 1 instead of A_2 = 1048577

@DaisukeMatsuzaki Thank you for pointing it out. I fixed it.

I think the second query should be A_2 = 1 instead of A_2 = 1048577

@DaisukeMatsuzaki Thank you for pointing it out. I fixed it.

I think the second query should be A_2 = 1 instead of A_2 = 1048577

@DaisukeMatsuzaki Thank you for pointing it out. I fixed it.

I think the second query should be A_2 = 1 instead of A_2 = 1048577

@DaisukeMatsuzaki Thank you for pointing it out. I fixed it.

I think the second query should be A_2 = 1 instead of A_2 = 1048577

=======
Suggestion 4

def main():
    N = 2**20
    A = [-1]*N
    Q = int(input())
    for _ in range(Q):
        t,x = map(int,input().split())
        if t == 1:
            h = x
            while A[h % N] != -1:
                h += 1
            A[h % N] = x
        else:
            print(A[x % N])

=======
Suggestion 5

def main():
    Q = int(input())
    A = [-1] * 2 ** 20
    h = 0
    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            while A[h % len(A)] != -1:
                h += 1
            A[h % len(A)] = x
        else:
            print(A[x % len(A)])

=======
Suggestion 6

def main():
    N = 2**20
    q = int(input())
    A = [-1] * N
    for _ in range(q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while A[h % N] != -1:
                h += 1
            A[h % N] = x
        else:
            print(A[x % N])

=======
Suggestion 7

def main():
    N = 2**20
    Q = int(input())
    A = [-1]*N
    for _ in range(Q):
        t,x = map(int,input().split())
        if t == 1:
            h = x
            while A[h%N] != -1:
                h += 1
            A[h%N] = x
        else:
            print(A[x%N])
    return

=======
Suggestion 8

def main():
    import sys
    input = sys.stdin.readline
    Q = int(input())
    A = [-1]*1048576
    for q in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while A[h%1048576] != -1:
                h += 1
            A[h%1048576] = x
        else:
            print(A[x%1048576])

=======
Suggestion 9

def main():
    # read input
    Q = int(input())
    queries = []
    for _ in range(Q):
        queries.append(list(map(int, input().split())))
    # solve
    N = 2 ** 20
    A = [-1] * N
    h = 0
    for t, x in queries:
        if t == 1:
            while A[h % N] != -1:
                h += 1
            A[h % N] = x
            h += 1
        else:
            print(A[x % N])
