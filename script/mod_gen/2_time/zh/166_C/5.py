def main():
    n,m = map(int,input().split())
    h = list(map(int,input().split()))
    ab = [list(map(int,input().split())) for _ in range(m)]
    ans = 0
    for i in range(m):
        if h[ab[i][0]-1] > h[ab[i][1]-1]:
            ans += 1
        elif h[ab[i][0]-1] < h[ab[i][1]-1]:
            ans += 1
        else:
            pass
    print(ans)

if __name__ == '__main__':
    main()