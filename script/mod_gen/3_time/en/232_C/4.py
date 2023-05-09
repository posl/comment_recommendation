def main():
    n, m = map(int, input().split())
    a = [tuple(map(int, input().split())) for _ in range(m)]
    c = [tuple(map(int, input().split())) for _ in range(m)]
    for i in range(2 ** n):
        p = []
        for j in range(n):
            if i >> j & 1:
                p.append(j + 1)
        if len(p) != n:
            continue
        for j in range(m):
            if (a[j][0] in p and a[j][1] in p) != (c[j][0] in p and c[j][1] in p):
                break
        else:
            print('Yes')
            return
    print('No')
main()

if __name__ == '__main__':
    main()