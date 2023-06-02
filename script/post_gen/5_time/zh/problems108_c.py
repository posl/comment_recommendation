Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    ans = 0
    for a in range(1, n+1):
        if a % k == 0:
            ans += n // k
        elif k % 2 == 0 and a % (k // 2) == k // 2:
            ans += (n - k // 2) // k + 1
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    ans = 0
    for a in range(1, N + 1):
        if a % K == 0:
            ans += N // K
        elif K % 2 == 0 and a % (K // 2) == K // 2:
            ans += N // K
        else:
            ans += N // K + 1
    print(ans)

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    ans = 0
    for a in range(1, n + 1):
        ans += (n // a) * max(0, a - k)
        ans += max(0, (n % a) - k + 1)
        if k == 0:
            ans -= 1
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    ans = 0
    for a in range(1, N+1):
        if a % K == 0:
            ans += N // K
        else:
            ans += N // K + 1
    if K % 2 == 0:
        for a in range(1, N+1):
            if a % K == K // 2:
                ans += N // K
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    ans = 0
    # a + b, b + c, c + a がすべて K の倍数であるとき、
    # a, b, c をそれぞれ K で割った余りをとると、
    # 余りの組み合わせは (0, 0, 0), (0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 1, 1), (1, 2, 0), (2, 0, 1), (2, 1, 0), (2, 2, 2) の 9 通り
    # 余りの組み合わせが決まれば、a, b, c が何通りあるかは自由に選べるので、
    # それぞれの余りの数をそれぞれの数で割った商の積が答え
    for a in range(1, N + 1):
        ans += (N // K + (a % K == 0)) ** 3
    print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    ans = 0
    # a + b, b + c, c + a がすべて K の倍数
    # a + b, b + c, c + a のそれぞれが K の倍数
    # a + b, b + c, c + a のそれぞれを K で割った余りが 0
    # a + b, b + c, c + a のそれぞれを K で割った余りの和が 0
    for i in range(1, N + 1):
        ans += (i % K) * ((N + K - i) // K)
        if K % 2 == 0:
            ans += (i % K) * (((N + K // 2 - i) // K) - ((N + K - i) // K))
    print(ans)

=======
Suggestion 7

def main():
    n,k = map(int,input().split())
    if k % 2 == 0:
        a = n // k
        b = (n + k // 2) // k
        print(a ** 3 + b ** 3)
    else:
        a = n // k
        print(a ** 3)

=======
Suggestion 8

def solve():
    N,K=map(int,input().split())
    ans=0
    for i in range(1,N+1):
        if i%K==0:
            ans+=1
        elif K%2==0 and i%K==K//2:
            ans+=1
    print(ans**3)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    ans = 0
    for a in range(1, N + 1):
        ans += ((N // a) + (0 if K % 2 else (N // (a * (K // 2))))) ** 3
    print(ans)

=======
Suggestion 10

def abc(n,k):
    ans = 0
    for a in range(1,n+1):
        for b in range(1,n+1):
            for c in range(1,n+1):
                if (a+b)%k == 0 and (b+c)%k == 0 and (c+a)%k == 0:
                    ans += 1
    return ans
