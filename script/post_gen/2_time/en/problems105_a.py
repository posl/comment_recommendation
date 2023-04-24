Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    if N % K == 0:
        print(0)
    else:
        print(1)

=======
Suggestion 2

def main():
    N, K = [int(x) for x in input().split()]
    if N % K == 0:
        print(0)
    else:
        print(1)

main()

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    print(0 if N % K == 0 else 1)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    print(N % K)

main()

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    print(N % K)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    print(1 if N%K else 0)

=======
Suggestion 7

def main():
    n,k = input().split()
    n = int(n)
    k = int(k)
    print(n%k)

main()
