def main():
    a,b,c,d,e,f,x = map(int,input().split())
    taka = 0
    aoki = 0
    while True:
        if taka >= x:
            print("Takahashi")
            break
        elif aoki >= x:
            print("Aoki")
            break
        else:
            taka += a
            aoki += d
        if
