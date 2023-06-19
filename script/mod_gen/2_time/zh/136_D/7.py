def main():
    S = input()
    N = len(S)
    ans = [0] * N
    for i in range(N-1):
        if S[i] == 'R' and S[i+1] == 'L':
            ans[i] += 1
            ans[i+1] += 1
    for i in range(N):
        if S[i] == 'R':
            if ans[i] % 2 == 0:
                ans[i+1] += ans[i] // 2
                ans[i] = 0
            else:
                ans[i+1] += ans[i] // 2
                ans[i] = 1
        else:
            if ans[i] % 2 == 0:
                ans[i-1] += ans[i] // 2
                ans[i] = 0
            else:
                ans[i-1] += ans[i] // 2
                ans[i] = 1
    print(" ".join(map(str, ans)))

if __name__ == '__main__':
    main()