def main():
    n, a, b = map(int, input().split())
    ans = 0
    ans += n // a
    ans += n // b
    ans -= n // (a*b)
    print(n*(n+1)//2 - ans*(ans+1)//2)
