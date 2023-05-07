def main():
    S = input()
    N = len(S)
    ans = [0] * N
    cnt = 0
    for i in range(N):
        if S[i] == 'R':
            cnt += 1
        else:
            ans[i] += (cnt + 1) // 2
            ans[i - 1] += cnt // 2
            cnt = 0
    print(*ans)

if __name__ == '__main__':
    main()