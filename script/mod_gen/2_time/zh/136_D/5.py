def solve():
    S = input()
    N = len(S)
    ans = [0] * N
    for i in range(N):
        if S[i] == 'R':
            for j in range(i + 1, N):
                if S[j] == 'L':
                    if (j - i) % 2 == 0:
                        ans[j] += 1
                    else:
                        ans[j - 1] += 1
                    break
        else:
            for j in range(i - 1, -1, -1):
                if S[j] == 'R':
                    if (i - j) % 2 == 0:
                        ans[j] += 1
                    else:
                        ans[j + 1] += 1
                    break
    print(' '.join(map(str, ans)))

if __name__ == '__main__':
    solve()