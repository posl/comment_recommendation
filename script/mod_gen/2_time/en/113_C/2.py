def main():
    N, M = map(int, input().split())
    P = [0] * M
    Y = [0] * M
    for i in range(M):
        P[i], Y[i] = map(int, input().split())
    P = np.array(P)
    Y = np.array(Y)
    P_sort = np.argsort(P)
    P = P[P_sort]
    Y = Y[P_sort]
    P_diff = np.diff(P)
    P_diff = np.append(P_diff, 1)
    P_diff = np.cumsum(P_diff)
    P_diff = np.append(0, P_diff)
    P_diff = P_diff[0:M]
    P_diff = P_diff.astype(np.str)
    P_diff = np.char.zfill(P_diff, 6)
    Y = Y.astype(np.str)
    Y = np.char.zfill(Y, 6)
    ans = P_diff + Y
    ans = ans.astype(np.int)
    ans_sort = np.argsort(ans)
    ans = ans[ans_sort]
    ans = ans.astype(np.str)
    ans = np.char.zfill(ans, 12)
    for i in range(M):
        print(ans[i])

if __name__ == '__main__':
    main()