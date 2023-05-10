def main():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(m)]
    k = int(input())
    c = [list(map(int, input().split())) for _ in range(k)]
    ans = 0
    for i in range(2 ** k):
        dish = [0] * (n + 1)
        for j in range(k):
            if (i >> j) & 1:
                dish[c[j][0]] += 1
            else:
                dish[c[j][1]] += 1
        tmp = 0
        for a_i, b_i in a:
            if dish[a_i] >= 1 and dish[b_i] >= 1:
                tmp += 1
        ans = max(ans, tmp)
    print(ans)

if __name__ == '__main__':
    main()