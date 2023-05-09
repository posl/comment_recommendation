def main():
    N = int(input())
    S = [input() for i in range(N)]
    T = [input() for i in range(N)]
    for i in range(N):
        for j in range(N):
            if S[i][j] == '#':
                Sx = i
                Sy = j
            if T[i][j] == '#':
                Tx = i
                Ty = j
    for i in range(4):
        for j in range(N):
            for k in range(N):
                if S[(j+Sx-Tx)%N][(k+Sy-Ty)%N] != T[j][k]:
                    break
            else:
                continue
            break
        else:
            print("Yes")
            break
        S = ["".join(list(reversed(S[i]))) for i in range(N)]
    else:
        print("No")

if __name__ == '__main__':
    main()