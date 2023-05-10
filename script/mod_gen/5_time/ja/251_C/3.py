def main():
    N = int(input())
    ST = []
    for i in range(N):
        s, t = input().split()
        ST.append([s, int(t)])
    ST.sort(key=lambda x: x[1], reverse=True)
    S = set()
    for i in range(N):
        S.add(ST[i][0])
    S = list(S)
    S.sort()
    T = []
    for i in range(len(S)):
        T.append([S[i], 0])
    for i in range(N):
        for j in range(len(S)):
            if ST[i][0] == T[j][0]:
                T[j][1] = max(T[j][1], ST[i][1])
                break
    for i in range(len(S)):
        if T[i][1] == 0:
            T[i][1] = 10 ** 9 + 1
    T.sort(key=lambda x: x[1], reverse=True)
    for i in range(len(S)):
        if T[0][1] == T[i][1]:
            print(i + 1)
            break

if __name__ == '__main__':
    main()