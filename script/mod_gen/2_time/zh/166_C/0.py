def main():
    n,m = map(int,input().split())
    h = list(map(int,input().split()))
    ab = [list(map(int,input().split())) for _ in range(m)]
    ans = 0
    for i in range(n):
        flag = True
        for j in range(m):
            if i+1 == ab[j][0] and h[i] <= h[ab[j][1]-1]:
                flag = False
                break
            elif i+1 == ab[j][1] and h[i] <= h[ab[j][0]-1]:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()