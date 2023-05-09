def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    k = int(input())
    cd = [list(map(int, input().split())) for _ in range(k)]
    ans = 0
    for i in range(2 ** k):
        dish = [0] * (n + 1)
        for j in range(k):
            if (i >> j) & 1:
                dish[cd[j][0]] += 1
            else:
                dish[cd[j][1]] += 1
        cnt = 0
        for a, b in ab:
            if dish[a] > 0 and dish[b] > 0:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)
main()

if __name__ == '__main__':
    main()