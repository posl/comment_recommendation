def main():
    n,a,b = map(int, input().split())
    ans = 0
    ans += n // a
    ans += n // b
    ans -= n // (a*b//gcd(a,b))
    print(ans)
