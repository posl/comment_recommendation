def main():
    a,b,c,d,e,f,x = map(int,input().split(" "))
    a = a*b
    c = c*b
    d = d*e
    f = f*e
    time = 0
    while True:
        if a > d:
            time += 1
            d += f
        elif a < d:
            time += 1
            a += c
        else:
            time += 1
            a += c
            d += f
        if time == x:
            break
    if a > d:
        print("青木")
    elif a < d:
        print("高桥")
    else:
        print("画")
