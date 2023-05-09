def main():
    n, m = map(int, input().split())
    xyz = []
    for i in range(n):
        xyz.append(list(map(int, input().split())))
    print(max([sum(sorted([sum([abs(xyz[i][j]) for i in range(n) if (i >> k) & 1]) for k in range(3)], reverse=True)[:m]) for j in range(3)]))

if __name__ == '__main__':
    main()