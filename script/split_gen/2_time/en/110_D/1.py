def main():
    N, M = map(int, input().split())
    MOD = 10**9 + 7
    ans = 1
    for i in range(2, int(M**0.5)+1):
        if M % i == 0:
            cnt = 0
            while M % i == 0:
                M //= i
                cnt += 1
            ans *= cnt + N - 1
            ans %= MOD
    if M > 1:
        ans *= N
        ans %= MOD
    print(ans)
