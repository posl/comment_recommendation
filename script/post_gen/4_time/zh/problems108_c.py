Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    ans = 0
    for a in range(1, N + 1):
        ans += (N // a) * max(0, a - K)
        ans += max(0, (N % a + 1) - K) if K > 0 else (N % a + 1)
    print(ans)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    ans = 0
    for i in range(1, n + 1):
        ans += n // i * max(0, (i - k))
        ans += max(0, (n % i + 1 - k))
    print(ans)

=======
Suggestion 3

def main():
    n,k = map(int,input().split())
    ans = 0
    for i in range(1,n+1):
        if i%k == 0:
            ans += n//k
        elif k%2 == 0 and i%k == k//2:
            ans += (n//k + 1)//2
    print(ans**3)

=======
Suggestion 4

def problems108_c():
    n,k = map(int,input().split())
    ans = 0
    for a in range(1,n+1):
        if a%k == 0:
            ans += n//k
        else:
            ans += n//k + 1
    print(ans)

problems108_c()

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    ans = 0
    for a in range(1, N + 1):
        ans += (N // a) * max(0, a - K)
        ans += max(0, (N % a) - K + 1)
    print(ans)

=======
Suggestion 6

def main():
    n,k = map(int,input().split())
    ans = 0
    if k%2 == 0:
        for i in range(1,n+1):
            if i%k == 0:
                ans += 1
        ans = ans**3
    else:
        for i in range(1,n+1):
            if i%k == 0:
                ans += 1
        for i in range(1,n+1):
            if i%k == k//2:
                ans += 1
        ans = ans**3
    print(ans)

=======
Suggestion 7

def main():
    # 读取输入
    n, k = map(int, input().split())
    # 定义变量
    ans = 0
    # 计算
    for a in range(1, n + 1):
        ans += (n // a) * max(0, a - k)
        ans += max(0, (n % a + 1) - k) if k > 0 else 0
    # 输出
    print(ans)

=======
Suggestion 8

def solve(N,K):
    ans = 0
    for a in range(1,N+1):
        if a % K == 0:
            ans += N // K
        else:
            ans += N // K + 1
    if K % 2 == 0:
        for a in range(1,N+1):
            if a % K == K // 2:
                ans += N // K
            else:
                ans += N // K + 1
    return ans

=======
Suggestion 9

def main():
    n,k = map(int,input().split())
    ans = 0
    # 1~n
    for i in range(1,n+1):
        # 1~k
        for j in range(1,k+1):
            if i%j == 0:
                # 1~k
                for l in range(1,k+1):
                    if i%l == 0:
                        ans += 1
    print(ans)

=======
Suggestion 10

def problems108_c():
    pass
