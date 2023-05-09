def main():
    n, k = map(int, input().split())
    p = []
    for i in range(n):
        p.append(list(map(int, input().split())))
    p.sort(key=lambda x: -x[0] - x[1] - x[2])
    print("Yes" if p[k - 1][0] + p[k - 1][1] + p[k - 1][2] >= p[k][0] + p[k][1] + p[k][2] else "No")

if __name__ == '__main__':
    main()