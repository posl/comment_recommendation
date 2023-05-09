def main():
    N = int(input())
    S = []
    T = []
    for _ in range(N):
        a,b = map(int, input().split())
        S.append([a,b])
    for _ in range(N):
        c,d = map(int, input().split())
        T.append([c,d])
    S.sort()
    T.sort()
    for i in range(N):
        for j in range(N):
            dx = T[j][0] - S[i][0]
            dy = T[j][1] - S[i][1]
            flag = True
            for k in range(N):
                if [S[k][0] + dx, S[k][1] + dy] not in T:
                    flag = False
                    break
            if flag:
                print("Yes")
                return
    print("No")

if __name__ == '__main__':
    main()