def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    ans = [0] * 10
    for i in range(10):
        x = 0
        y = 0
        for a in A:
            if a + x + y == i:
                x += 1
            elif (a * x + y) % 10 == i:
                y += 1
        ans[i] = x * y % MOD
    print(*ans, sep='\n')
