def main():
    a,b,c,d = map(int,input().split())
    if a > b*d:
        print(-1)
        return
    if b <= c*d:
        print(1)
        return
    print((a+d*b-1)//(b+c*d)+1)
