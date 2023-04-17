Synthesizing 10/10 solutions

=======

def main():
    N,K = map(int,input().split())
    cnt = 0
    for a in range(1,N+1):
        for b in range(1,N+1):
            for c in range(1,N+1):
                if (a+b)%K == 0 and (b+c)%K == 0 and (c+a)%K == 0:
                    cnt += 1
    print(cnt)

=======

def main():
    N, K = map(int, input().split())
    cnt = 0
    for a in range(1, N+1):
        for b in range(1, N+1):
            if (a + b) % K == 0:
                cnt += N // K
                if (N % K) >= (a + b) // K:
                    cnt += 1
    print(cnt**2)

=======

def main():
    N, K = map(int, input().split())
    #N, K = 3, 2
    #N, K = 5, 3
    #N, K = 31415, 9265
    #N, K = 35897, 932
    #N, K = 100000, 100000
    #N, K = 100000, 1
    #N, K = 100000, 10
    #N, K = 100000, 100
    #N, K = 100000, 1000
    #N, K = 100000, 10000
    #N, K = 100000, 100000
    #N, K = 100000, 1000000
    #N, K = 100000, 10000000
    #N, K = 100000, 100000000
    #N, K = 100000, 1000000000
    #N, K = 100000, 10000000000
    #N, K = 100000, 100000000000
    #N, K = 100000, 1000000000000
    #N, K = 100000, 10000000000000
    #N, K = 100000, 100000000000000
    #N, K = 100000, 1000000000000000
    #N, K = 100000, 10000000000000000
    #N, K = 100000, 100000000000000000
    #N, K = 100000, 1000000000000000000
    #N, K = 100000, 10000000000000000000
    #N, K = 100000, 100000000000000000000
    #N, K = 100000, 1000000000000000000000
    #N, K = 100000, 10000000000000000000000
    #N, K = 100000, 100000000000000000000000
    #N, K = 100000, 1000000000000000000000000
    #N,

=======

def main():
    N, K = map(int, input().split())
    ans = 0
    for a in range(1, N+1):
        for b in range(1, N+1):
            c = K - (a+b)
            if 1 <= c <= N:
                ans += 1
    print(ans)

=======

def main():
    n,k = map(int,input().split())
    ans = 0
    for a in range(1,n+1):
        for b in range(1,n+1):
            c = a + b
            if c % k == 0:
                ans += 1
    print(ans*n)

=======

def main():
    n,k = map(int,input().split())
    ans = 0
    for i in range(1,n+1):
        ans += (n//i) * max(0,i-k+1) + max(0,n%i-k+1)
    if k == 0:
        ans -= n
    print(ans)

=======

def main():
    #入力
    N,K = map(int,input().split())
    #処理
    answer = 0
    for a in range(1,N+1):
        for b in range(1,N+1):
            c = a+b
            if c%K == 0:
                answer += N//K
                if b%K == 0:
                    answer += 1
    #出力
    print(answer)

=======

def main():
    N,K = map(int,input().split())
    a = N//K
    b = N//K
    c = N//K
    if K%2 == 0:
        d = N//K
        e = N//K
        f = N//K
        if N%K >= K//2:
            d = d + 1
        if N%K >= K//2:
            e = e + 1
        if N%K >= K//2:
            f = f + 1
        print(a**3+b**3+c**3-d**3-e**3-f**3)
    else:
        print(a**3)

=======

def main():
    #入力
    N, K = map(int, input().split())
    #出力
    print((N//K)**3 + (N//K)**3 + (N//K)**3 + (N//K)**3)

=======

def main():
    #入力
    N, K = map(int, input().split())
    #変数の初期化
    cnt = 0
    #計算
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                if (i + j) % K == 0 and (j + k) % K == 0 and (k + i) % K == 0:
                    cnt += 1
    #出力
    print(cnt)
