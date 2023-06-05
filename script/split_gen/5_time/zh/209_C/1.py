def main():
    n = int(input())
    c = list(map(int, input().split()))
    m = 10**9 + 7
    c.sort()
    ans = 1
    for i in range(n):
        ans *= c[i] - i
        ans %= m
    print(ans)
