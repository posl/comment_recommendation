def main():
    a,b,c,d,e,f,x = map(int,input().split())
    taka = 0
    aoki = 0
    for i in range(x):
        if i % (a+b) < a:
            taka += 1
        if i % (d+e) < d:
            aoki += 1
    if taka > aoki:
        print("高桥")
    elif taka < aoki:
        print("青木")
    else:
        print("画")
