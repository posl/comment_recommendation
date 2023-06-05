def main():
    a,b,c,d,e,f,x = map(int, input().split())
    taka = 0
    aoki = 0
    for i in range(0,x):
        if i%(a+b) < a:
            taka = taka + e
        if i%(c+d) < d:
            aoki = aoki + f
    if taka > aoki:
        print("高桥")
    elif taka < aoki:
        print("青木")
    else:
        print("画")

if __name__ == '__main__':
    main()