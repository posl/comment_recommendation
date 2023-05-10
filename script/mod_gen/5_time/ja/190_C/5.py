def main():
    n, m = map(int, input().split())
    a = [0 for _ in range(m)]
    b = [0 for _ in range(m)]
    for i in range(m):
        a[i], b[i] = map(int, input().split())
    k = int(input())
    c = [0 for _ in range(k)]
    d = [0 for _ in range(k)]
    for i in range(k):
        c[i], d[i] = map(int, input().split())
    ans = 0
    for i in range(2 ** k):
        dish = [0 for _ in range(n)]
        for j in range(k):
            if (i >> j) & 1:
                dish[d[j] - 1] += 1
            else:
                dish[c[j] - 1] += 1
        cnt = 0
        for j in range(m):
            if dish[a[j] - 1] > 0 and dish[b[j] - 1] > 0:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

if __name__ == '__main__':
    main()