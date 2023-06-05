def main():
    s = input()
    n = len(s)
    ans = [0] * n
    cnt = 0
    for i in range(n):
        if s[i] == 'R':
            cnt += 1
        else:
            ans[i] += cnt // 2
            ans[i - 1] += (cnt + 1) // 2
            cnt = 0
    print(*ans)

if __name__ == '__main__':
    main()