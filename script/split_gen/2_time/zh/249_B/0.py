def main():
    a,b,c,d,e,f,x = map(int,input().split())
    taka = a
    aoki = d
    for i in range(x):
        if i % (a+b) < a:
            taka += e
        if i % (c+d) < d:
            aoki += f
    if taka > aoki:
        print("高桥")
    elif taka < aoki:
        print("青木")
    else:
        print("画")
