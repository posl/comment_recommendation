def main():
    n = int(input())
    s = input()
    w = list(map(int, input().split()))
    l = 0
    r = 10**9 + 1
    while r - l > 1:
        m = (l + r) // 2
        cnt = 0
        for i in range(n):
            if (s[i] == '0' and w[i] < m) or (s[i] == '1' and w[i] >= m):
                cnt += 1
        if cnt == n:
            l = m
        else:
            r = m
    print(l)

if __name__ == '__main__':
    main()