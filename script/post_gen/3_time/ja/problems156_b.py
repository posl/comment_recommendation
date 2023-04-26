Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    ans = 0
    while N > 0:
        N //= K
        ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    print(len(str(N)))

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    print(len(str(n)))

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    print(len(str(N).encode('utf-8').hex())*4//len(bin(K)[2:]))

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    print(len(str(n)) + 1)

=======
Suggestion 6

def main():
    N,K = map(int,input().split())
    ans = len(str(N))
    print(ans)
    return
