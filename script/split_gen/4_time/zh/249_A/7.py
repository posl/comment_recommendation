def main():
    a,b,c,d,e,f,x = map(int, input().split())
    taka = 0
    aoki = 0
    while x > 0:
        if a > 0:
            taka += b
            a -= 1
        else:
            a += c
        if d > 0:
            aoki += e
            d -= 1
        else:
            d += f
        x -= 1
    if taka > aoki:
        print("高桥")
    elif taka < aoki:
        print("青木")
    else:
        print("画")
