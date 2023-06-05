def run():
    a,b,c,d,e,f,x = map(int, input().split())
    taka = 0
    aoki = 0
    for i in range(10000):
        if i % (a+b+c) < a:
            taka += 1
        if i % (d+e+f) < d:
            aoki += 1
        if taka * x > aoki * x:
            print("高桥")
            return
        elif taka * x < aoki * x:
            print("青木")
            return
    print("画")
