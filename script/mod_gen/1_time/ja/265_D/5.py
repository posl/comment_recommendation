def main():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    # 累積和
    S = [0]
    for a in A:
        S.append(S[-1] + a)
    # 累積和の差
    D = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(i, N):
            D[i][j] = S[j+1] - S[i]
    # 答え
    ans = False
    # 1つ目の区間を固定
    for i in range(N-3):
        # 2つ目の区間を固定
        for j in range(i+1, N-2):
            # 3つ目の区間を固定
            for k in range(j+1, N-1):
                # 1つ目の区間と2つ目の区間の和
                p = D[0][i]
                # 2つ目の区間と3つ目の区間の和
                q = D[j][k]
                # 3つ目の区間と4つ目の区間の和
                r = D[k+1][N-1]
                # それぞれの和が条件を満たすか
                if p == P and q == Q and r == R:
                    ans = True
    if ans:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()