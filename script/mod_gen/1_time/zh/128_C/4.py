def main():
    n,m = map(int,input().split())
    k = []
    for _ in range(m):
        k.append(list(map(int,input().split()))[1:])
    p = list(map(int,input().split()))
    ans = 0
    for i in range(2**n):
        light = [0]*m
        for j in range(n):
            if (i>>j)&1 == 1:
                for l in range(m):
                    if j+1 in k[l]:
                        light[l] += 1
        if light == p:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()