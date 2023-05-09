def main():
    a,b,c = map(int,input().split())
    ans = 0
    ans += a/(a+b+c)
    ans += b/(a+b+c)
    ans += c/(a+b+c)
    print(100/ans-1)
