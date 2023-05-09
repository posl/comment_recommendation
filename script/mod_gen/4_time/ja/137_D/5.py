def main():
    N, M = map(int, input().split())
    ab = []
    for i in range(N):
        ab.append(list(map(int, input().split())))
    ab.sort(key=lambda x:x[0])
    ans = 0
    for i in range(N):
        if ab[i][0] <= M:
            ans += ab[i][1]
            M -= ab[i][0]
        else:
            ans += M * ab[i][1]
            break
    print(ans)

if __name__ == '__main__':
    main()