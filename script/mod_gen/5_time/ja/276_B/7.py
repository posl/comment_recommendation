def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    ab.sort(key=lambda x:(x[0], x[1]))
    cnt = 0
    for i in range(1, n+1):
        for j in range(m):
            if ab[j][0] == i:
                cnt += 1
            else:
                break
        print(cnt, end=' ')
        for j in range(m):
            if ab[j][0] == i:
                print(ab[j][1], end=' ')
            else:
                break
        print()
        ab = ab[cnt:]
        cnt = 0

if __name__ == '__main__':
    main()