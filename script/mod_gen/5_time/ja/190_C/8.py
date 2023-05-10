def main():
    n,m = list(map(int, input().split()))
    ab = []
    for i in range(m):
        ab.append(list(map(int, input().split())))
    k = int(input())
    cd = []
    for i in range(k):
        cd.append(list(map(int, input().split())))
    ans = 0
    for i in range(2**k):
        tmp = [0]*n
        for j in range(k):
            if ((i>>j)&1):
                tmp[cd[j][0]-1] += 1
            else:
                tmp[cd[j][1]-1] += 1
        cnt = 0
        for j in range(m):
            if tmp[ab[j][0]-1] and tmp[ab[j][1]-1]:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

if __name__ == '__main__':
    main()