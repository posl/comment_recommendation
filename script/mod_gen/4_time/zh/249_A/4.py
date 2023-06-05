def main():
    a,b,c,d,e,f,x = map(int,input().split())
    taka = 0
    aoki = 0
    t = 0
    while t < x:
        if t % (a+b) < a:
            taka += 1
        if t % (d+e) < d:
            aoki += 1
        t += 1
    if taka > aoki:
        print("高桥")
    elif taka < aoki:
        print("青木")
    else:
        print("画")

if __name__ == '__main__':
    main()