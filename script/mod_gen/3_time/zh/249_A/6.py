def main():
    A,B,C,D,E,F,X = map(int, input().split())
    time = 0
    while X > 0:
        if A > 0:
            X -= B
            time += A
        if X <= 0:
            break
        X -= C
        if X <= 0:
            break
        if D > 0:
            X -= E
            time += D
        if X <= 0:
            break
        X -= F
    if time > 0:
        print("高桥")
    elif time < 0:
        print("青木")
    else:
        print("画")

if __name__ == '__main__':
    main()