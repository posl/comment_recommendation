def check():
    D, T, S = input().split()
    D = int(D)
    T = int(T)
    S = int(S)
    if D <= T * S:
        print("Yes")
    else:
        print("No")
check()

if __name__ == '__main__':
    check()