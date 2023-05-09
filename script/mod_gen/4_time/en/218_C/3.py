def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        S.append(input())
    for i in range(N):
        T.append(input())
    for i in range(4):
        if S == T:
            print("Yes")
            exit()
        S = rotate(S)
    print("No")

if __name__ == '__main__':
    main()