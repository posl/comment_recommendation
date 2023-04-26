Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N + 1):
        for j in range(1, K + 1):
            ans += i * 100 + j
    print(ans)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    ans = 0
    for i in range(1, n+1):
        for j in range(1, k+1):
            ans += int(str(i) + '0' + str(j))
    print(ans)

=======
Suggestion 3

def main():
    n,k = map(int,input().split())
    ans = 0
    for i in range(1,n+1):
        for j in range(1,k+1):
            ans += i*100+j
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    sum = 0
    for i in range(1, N+1):
        for j in range(1, K+1):
            sum += i*100 + j
    print(sum)

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    sum = 0
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            sum += int(str(i) + '0' + str(j))
    print(sum)

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    print(sum([int(str(i) + str(j)) for i in range(1, n + 1) for j in range(1, k + 1)]))

=======
Suggestion 7

def calc(N,K):
    ans = 0
    for i in range(1,N+1):
        for j in range(1,K+1):
            ans += int(str(i) + '0' + str(j))
    return ans

=======
Suggestion 8

def main():
    # 標準入力から N, K を取得する
    N, K = map(int, input().split())

    # N と K を 3 桁の整数とみなして、部屋番号の合計を計算する
    # N は 1 桁なので 100 を掛ける
    # K は 1 桁なので 10 を掛ける
    print(N * 100 * (N * 100 + K * 10 + K))

=======
Suggestion 9

def main():
    N,K = map(int,input().split())
    print(N*100*K*(K+1)//2)

=======
Suggestion 10

def main():
    n, k = map(int, input().split())
    print( (n*100 + k*10)*n + k*10 )
