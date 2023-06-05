def main():
    n = int(input())
    an = list(map(int, input().split()))
    mod = 998244353
    ans = 0
    for i in range(1 << n):
        sm = 0
        for j in range(n):
            if i & (1 << j):
                sm += an[j]
        if sm % 2 == 0:
            ans += 1
    print(ans % mod)
