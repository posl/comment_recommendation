def main():
    n, m = map(int, input().split())
    ab = []
    for i in range(m):
        ab.append(list(map(int, input().split())))
    k = int(input())
    cd = []
    for i in range(k):
        cd.append(list(map(int, input().split())))
    ans = 0
    for i in range(2**k):
        dish = [0 for i in range(n)]
        for j in range(k):
            if (i >> j) & 1:
                dish[cd[j][0]-1] += 1
            else:
                dish[cd[j][1]-1] += 1
        tmp = 0
        for j in range(m):
            if dish[ab[j][0]-1] > 0 and dish[ab[j][1]-1] > 0:
                tmp += 1
        ans = max(ans, tmp)
    print(ans)

if __name__ == '__main__':
    main()