def main():
    H,W = map(int,input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    S_count = [[0] * W for _ in range(H)]
    T_count = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                S_count[i][j] = 1
            else:
                S_count[i][j] = 0
            if T[i][j] == "#":
                T_count[i][j] = 1
            else:
                T_count[i][j] = 0
    S_sum = sum([sum(i) for i in S_count])
    T_sum = sum([sum(i) for i in T_count])
    if S_sum != T_sum:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()