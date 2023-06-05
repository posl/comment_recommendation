def main():
    a,b,c,d,e,f,x = map(int,input().split())
    taka = 0
    aoki = 0
    while True:
        taka += a
        if taka >= x:
            print("高桥")
            break
        aoki += d
        if aoki >= x:
            print("青木")
            break
        taka -= c
        aoki -= f
        if taka >= x and aoki >= x:
            print("画")
            break
