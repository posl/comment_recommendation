def main():
    a,b,c,d,e,f,x = map(int, input().split())
    # print(a,b,c,d,e,f,x)
    taka = 0
    aoki = 0
    while True:
        if x <= 0:
            break
        if a > 0:
            taka += b
            a -= 1
            x -= 1
        else:
            x -= 1
        if x <= 0:
            break
        if d > 0:
            a
