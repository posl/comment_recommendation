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
                S_x = i
                S_y = j
                break
    for i in range(N):
        for j in range(N):
            if T[i][j] == '#':
                T_x = i
                T_y = j
                break
    for i in range(4):
        for j in range(N):
            for k in range(N):
                if S[j][k] == '#':
                    S_x = j
                    S_y = k
                    break
        for j in range(N):
            for k in range(N):
                if T[j][k] == '#':
                    T_x = j
                    T_y = k
                    break
        if S_x - T_x == S_y - T_y:
            for j in range(N):
                for k in range(N):
                    if S[j][k] == '#' and T[j + S_x - T_x][k + S_y - T_y] != '#':
                        break
                else:
                    continue
                break
            else:
                print('Yes')
                break
        S = list(map(list, zip(*S[::-1])))
    else:
        print('No')

if __name__ == '__main__':
    main()