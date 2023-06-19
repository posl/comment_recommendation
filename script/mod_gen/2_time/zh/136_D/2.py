def main():
    S = input()
    N = len(S)
    ans = [0] * N
    for i in range(N-1):
        if S[i] == 'R':
            if S[i+1] == 'R':
                ans[i+1] += ans[i] + 1
                ans[i] = 0
        else:
            ans[i+1] += ans[i]
    for i in range(N-1, 0, -1):
        if S[i] == 'L':
            if S[i-1] == 'L':
                ans[i-1] += ans[i] + 1
                ans[i] = 0
        else:
            ans[i-1] += ans[i]
    print(' '.join(map(str, ans)))
main()
