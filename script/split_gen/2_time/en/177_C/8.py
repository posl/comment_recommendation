def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    mod = 10**9 + 7
    a.sort()
    s = 0
    for i in range(n-1):
        s += (a[i] * (a[i+1] - a[i]) * (n - i - 1)) % mod
        s %= mod
    print(s)
