def main():
    n, k = map(int, input().split())
    s = [int(i) for i in input()]
    ans = 0
    cnt = 0
    for i in range(n):
        if s[i] == 0:
            cnt += 1
        else:
            cnt = 0
        ans = max(ans, cnt)
    ans += k
    if ans > n:
        ans = n
    print(ans)

if __name__ == '__main__':
    main()