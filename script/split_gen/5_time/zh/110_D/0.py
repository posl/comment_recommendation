def main():
    N, M = map(int, input().split())
    ans = 1
    i = 2
    while i * i <= M:
        cnt = 0
        while M % i == 0:
            cnt += 1
            M //= i
        ans *= N + cnt - 1
        ans %= 10**9 + 7
        i += 1
    if M != 1:
        ans *= N
        ans %= 10**9 + 7
    print(ans)
