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

def main():
    n,d = map(int, input().split())
    if n%(2*d+1) == 0:
        print(n//(2*d+1))
    else:
        print(n//(2*d+1)+1)

=======
Suggestion 3

def main():
    N, D = map(int, input().split())
    print((N + 2 * D) // (2 * D + 1))

=======
Suggestion 4

def problems134_b():
    n, d = map(int, input().split())
    print((n + 2 * d) // (2 * d + 1))

=======
Suggestion 5

def main():
    N, D = map(int, input().split())
    print(int(N/(D*2+1))+1 if N%(D*2+1) != 0 else int(N/(D*2+1)))

=======
Suggestion 6

def main():
    n, d = map(int, input().split())
    print((n + (2 * d)) // ((2 * d) + 1))

=======
Suggestion 7

def problem134_b():
    N, D = map(int, input().split())
    print((N + 2 * D) // (2 * D + 1))

=======
Suggestion 8

def main():
    N, D = map(int, input().split())
    print(-(-N//(2*D+1)))
