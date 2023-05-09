def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        S.append(list(map(int, input().split())))
    for i in range(N):
        T.append(list(map(int, input().split())))
    for i in range(4):
        if S == T:
            print("Yes")
            return
        for j in range(N):
            S[j][0], S[j][1] = S[j][1], -S[j][0]
    for i in range(4):
        if S == T:
            print("Yes")
            return
        for j in range(N):
            S[j][0], S[j][1] = -S[j][1], S[j][0]
    print("No")

if __name__ == '__main__':
    main()