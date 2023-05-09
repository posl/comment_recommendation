def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        S.append(list(map(int, input().split())))
    for i in range(N):
        T.append(list(map(int, input().split())))
    S = sorted(S)
    T = sorted(T)
    for i in range(N):
        S[i][0] -= S[0][0]
        S[i][1] -= S[0][1]
        T[i][0] -= T[0][0]
        T[i][1] -= T[0][1]
    for i in range(360):
        for j in range(N):
            S[j][0], S[j][1] = S[j][0]*cos(i*pi/180)-S[j][1]*sin(i*pi/180), S[j][0]*sin(i*pi/180)+S[j][1]*cos(i*pi/180)
        S = sorted(S)
        for j in range(N):
            S[j][0] = round(S[j][0], 6)
            S[j][1] = round(S[j][1], 6)
        if S == T:
            print("Yes")
            return
    print("No")
    return

if __name__ == '__main__':
    main()