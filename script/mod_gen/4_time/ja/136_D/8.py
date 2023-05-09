def main():
    S = input()
    N = len(S)
    ans = [0] * N
    # Rがある場所を探す
    R_index = []
    for i in range(N):
        if S[i] == 'R':
            R_index.append(i)
    # Rがない場合
    if len(R_index) == 0:
        for i in range(N):
            ans[i] = N
    # Rがある場合
    else:
        for i in range(N):
            # Rの左端の場合
            if i == 0:
                # 1回の移動で右に行く
                ans[R_index[0]] += 1
            # Rの右端の場合
            elif i == N - 1:
                # 1回の移動で左に行く
                ans[R_index[-1]] += 1
            # Rの間の場合
            else:
                # Rの左端にいる場合
                if S[i] == 'R':
                    # 1回の移動で右に行く
                    ans[R_index[0]] += 1
                    # 1回の移動で左に行く
                    ans[R_index[0] - 1] += 1
                # Rの右端にいる場合
                elif S[i] == 'L':
                    # 1回の移動で左に行く
                    ans[R_index[-1]] += 1
                    # 1回の移動で右に行く
                    ans[R_index[-1] + 1] += 1
    print(*ans)

if __name__ == '__main__':
    main()