Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    ans = 0
    for i in range(1, n+1):
        for j in range(1, k+1):
            ans += i*100 + j
    print(ans)

=======
Suggestion 2

def main():
    N,K = map(int,input().split())
    ans = 0
    for i in range(1,N+1):
        for j in range(1,K+1):
            ans += i*100 + j
    print(ans)

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    result = 0
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            result += i * 100 + j
    print(result)

=======
Suggestion 4

def solve():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N+1):
        for j in range(1, K+1):
            ans += i * 100 + j
    print(ans)

=======
Suggestion 5

def problems203_b():
    n, k = map(int, input().split())
    sum = 0
    for i in range(1, n+1):
        for j in range(1, k+1):
            sum += int(str(i) + '0' + str(j))
    print(sum)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    result = 0
    for i in range(N):
        for j in range(K):
            result += (i+1)*100 + (j+1)
    print(result)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    print(sum([int(str(i) + str(j) + str(k)) for i in range(1, N+1) for j in range(1, K+1) for k in range(1, K+1)]))

=======
Suggestion 8

def main():
    n,k = map(int, input().split())
    s = 0
    for i in range(1, n+1):
        for j in range(1, k+1):
            s += int(str(i) + "0" + str(j))
    print(s)

=======
Suggestion 9

def main():
    n, k = map(int, input().split())
    print((n * k * (n + 1) * k) // 2)
