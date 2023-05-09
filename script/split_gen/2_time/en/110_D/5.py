def main():
    N, M = map(int, input().split())
    mod = 10**9+7
    ans = 1
    for i in range(2, M+1):
        if i*i > M:
            break
        cnt = 0
        while M % i == 0:
            M //= i
            cnt += 1
        ans *= cnt + 1
        ans %= mod
    if M > 1:
        ans *= 2
        ans %= mod
    print(ans)
