def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9+7
    ans = 0
    for i in range(60):
        o = 0
        for a in A:
            if a>>i&1:
                o += 1
        ans += o*(N-o)*2**i
        ans %= MOD
    print(ans)
