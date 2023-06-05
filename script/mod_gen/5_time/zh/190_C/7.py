def main():
    n,m = map(int,input().split())
    ab = [list(map(int,input().split())) for _ in range(m)]
    k = int(input())
    cd = [list(map(int,input().split())) for _ in range(k)]
    ans = 0
    for i in range(2**k):
        dish = [0] * (n+1)
        for j in range(k):
            if (i >> j) & 1:
                dish[cd[j][0]] += 1
            else:
                dish[cd[j][1]] += 1
        sum = 0
        for l in range(m):
            if dish[ab[l][0]] >= 1 and dish[ab[l][1]] >= 1:
                sum += 1
        ans = max(ans,sum)
    print(ans)

if __name__ == '__main__':
    main()