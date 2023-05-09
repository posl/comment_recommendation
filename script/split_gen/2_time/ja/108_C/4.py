def main():
    N, K = map(int, input().split())
    ans = 0
    for a in range(1, N + 1):
        b = c = a
        if (a + b) % K == 0 and (b + c) % K == 0 and (c + a) % K == 0:
            ans += 1
    print(ans)
