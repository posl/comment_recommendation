def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        S.append(input())
    for i in range(N):
        T.append(input())
    for i in range(N):
        for j in range(N):
            if S[i][j] == '#':
                a = i
                b = j
                break
    for i in range(N):
        for j in range(N):
            if T[i][j] == '#':
                c = i
                d = j
                break
    for i in range(N):
        for j in range(N):
            if (a - c + i) < 0 or (a - c + i) >= N or (b - d + j) < 0 or (b - d + j) >= N or S[a - c + i][b - d + j] != T[i][j]:
                break
        else:
            continue
        break
    else:
        print('Yes')
        return
    for i in range(N):
        for j in range(N):
            if (a - c + i) < 0 or (a - c + i) >= N or (b - d + j) < 0 or (b - d + j) >= N or S[a - c + i][b - d + j] != T[N - 1 - j][i]:
                break
        else:
            continue
        break
    else:
        print('Yes')
        return
    for i in range(N):
        for j in range(N):
            if (a - c + i) < 0 or (a - c + i) >= N or (b - d + j) < 0 or (b - d + j) >= N or S[a - c + i][b - d + j] != T[N - 1 - i][N - 1 - j]:
                break
        else:
            continue
        break
    else:
        print('Yes')
        return
    for i in range(N):
        for j in range(N):
            if (a - c + i) < 0 or (a - c + i) >= N or (b - d + j) < 0 or (b - d + j) >= N or S[a - c + i][b - d + j]

if __name__ == '__main__':
    main()