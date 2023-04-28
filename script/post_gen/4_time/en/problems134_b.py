Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, D = map(int, input().split())
    if N % (2 * D + 1) == 0:
        print(N // (2 * D + 1))
    else:
        print(N // (2 * D + 1) + 1)

=======
Suggestion 2

def solve():
    N, D = map(int, input().split())
    if N % (2 * D + 1) == 0:
        print(N // (2 * D + 1))
    else:
        print(N // (2 * D + 1) + 1)

=======
Suggestion 3

def main():
    N, D = map(int, input().split())
    print((N + 2 * D) // (2 * D + 1))

=======
Suggestion 4

def main():
    n, d = map(int, input().split())
    print(n//(2*d+1) if n%(2*d+1) == 0 else n//(2*d+1)+1)

=======
Suggestion 5

def problems134_b():
    n, d = map(int, input().split())
    print((n + 2 * d) // (2 * d + 1))

=======
Suggestion 6

def main():
    N, D = map(int, input().split())
    print((N + D * 2) // (D * 2 + 1))

=======
Suggestion 7

def problems134_b():
    n, d = map(int, input().split())
    print((n + (2 * d)) // ((2 * d) + 1))

=======
Suggestion 8

def count_inspectors(N, D):
    inspectors = 0
    for i in range(N):
        if i % (2 * D + 1) == 0:
            inspectors += 1
    return inspectors
