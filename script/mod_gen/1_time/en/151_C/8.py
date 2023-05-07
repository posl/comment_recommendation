def main():
    N, M = map(int, input().split())
    S = [list(input().split()) for _ in range(M)]
    S.reverse()
    ans = [0, 0]
    AC = [0] * (N + 1)
    for i in range(M):
        if AC[int(S[i][0])] == 0:
            if S[i][1] == 'AC':
                AC[int(S[i][0])] = 1
                ans[0] += 1
            else:
                ans[1] += 1
        else:
            if S[i][1] == 'AC':
                continue
            else:
                ans[1] += 1
    print(ans[0], ans[1])

if __name__ == '__main__':
    main()