def main():
    a,b,x = map(int,input().split())
    if a*a*b/2 <= x:
        ans = 90 - (a*a*b-x)*2/(a*a*a)
    else:
        ans = (a*b*b)/(2*x)
    print(ans)
