def main():
    A,B,C,D,E,F,X = map(int,input().split())
    T = 0
    while True:
        if A > B:
            T += B
            A -= B
        else:
            T += A
            A = 0
        if T >= X:
            print("高桥")
            break
        T += C
        if D > E:
            T += E
            D -= E
        else:
            T += D
            D = 0
        if T >= X:
            print("青木")
            break
        T += F
        if A == D:
            print("画")
            break

if __name__ == '__main__':
    main()