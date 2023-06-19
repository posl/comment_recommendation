def main():
    S = input()
    N = len(S)
    ans = [0] * N
    for i in range(N):
        if S[i] == 'R':
            # Rの左側にいる人数
            ans[i+1] += ans[i]
            ans[i] = 0
        else:
            # Lの右側にいる人数
            ans[i-1] += ans[i]
            ans[i] = 0
    print(' '.join([str(x) for x in ans]))
