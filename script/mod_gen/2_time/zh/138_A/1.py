def main():
    n, m = map(int, input().split())
    # print(n, m)
    ab = []
    for i in range(n):
        ab.append(list(map(int, input().split())))
    # print(ab)
    ab.sort(key=lambda x: x[0])
    # print(ab)
    ans = 0
    for i in range(n):
        if ab[i][0] <= m:
            ans += ab[i][1]
            m -= ab[i][0]
        else:
            ans += m * ab[i][1]
            break
    print(ans)

if __name__ == '__main__':
    main()