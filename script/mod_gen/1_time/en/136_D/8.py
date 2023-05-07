def main():
    S = input()
    L = len(S)
    ans = [0] * L
    i = 0
    while i < L:
        if S[i] == 'R':
            cnt = 0
            while i < L and S[i] == 'R':
                cnt += 1
                i += 1
            if cnt % 2 == 0:
                ans[i-1] += cnt // 2
                ans[i] += cnt // 2
            else:
                ans[i-1] += cnt // 2 + 1
                ans[i] += cnt // 2
        else:
            cnt = 0
            while i < L and S[i] == 'L':
                cnt += 1
                i += 1
            if cnt % 2 == 0:
                ans[i-1] += cnt // 2
                ans[i-2] += cnt // 2
            else:
                ans[i-1] += cnt // 2
                ans[i-2] += cnt // 2 + 1
    print(*ans)

if __name__ == '__main__':
    main()