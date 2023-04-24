Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    ans = 0
    while N > 0:
        ans += 1
        N //= K
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
    print(len(str(N).encode('utf-8').hex()) * 4 // len(bin(K)[2:]))

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    print(len(str(N).split(K)))

=======
Suggestion 6

def main():
    n,k = map(int,input().split()) #nをk進数で表したときの桁数を求める
    cnt = 0
    while n != 0:
        n //= k
        cnt += 1
    print(cnt)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    print(len(str(N)))
    print(len(str(N)) if N == 0 else len(str(N)) - 1)
