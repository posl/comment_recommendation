def main():
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    ab = [list(map(int, input().split())) for _ in range(m)]
    ans = 0
    for i in range(n):
        for j in range(m):
            if ab[j][0] == i+1 and h[i] <= h[ab[j][1]-1]:
                break
            if ab[j][1] == i+1 and h[i] <= h[ab[j][0]-1]:
                break
        else:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()