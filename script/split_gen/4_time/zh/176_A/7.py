def main():
    n,x,t = map(int,input().split())
    ans = n // x * t
    if n % x != 0:
        ans += t
    print(ans)
