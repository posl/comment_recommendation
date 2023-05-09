def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 998244353
    ans = 0
    for i in range(1, 1 << N):
        s = 0
        for j in range(N):
            if i & (1 << j):
                s += A[j]
        if s % bin(i).count("1") == 0:
            ans += 1
    print(ans % mod)
