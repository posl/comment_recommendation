def main():
    N, M = map(int, input().split())
    XYZ = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(2 ** 3):
        XYZ.sort(key=lambda x: sum(x[j] * (-1 if (i >> j) & 1 else 1) for j in range(3)))
        ans = max(ans, sum(sum(x[j] * (-1 if (i >> j) & 1 else 1) for j in range(3)) for x in XYZ[:M]))
    print(ans)

if __name__ == '__main__':
    main()