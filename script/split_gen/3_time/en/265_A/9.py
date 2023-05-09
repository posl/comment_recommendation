def main():
    #input
    x,y,n = map(int,input().split())
    #calculations
    ans = 0
    if x * n < y:
        ans = x * n
    else:
        ans = y * (n // 3)
        if x * (n % 3) < y:
            ans += x * (n % 3)
        else:
            ans += y
    #output
    print(ans)
