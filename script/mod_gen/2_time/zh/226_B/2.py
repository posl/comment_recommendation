def main():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    d = {}
    for i in range(n):
        a[i].pop(0)
        d.setdefault(tuple(a[i]), 0)
        d[tuple(a[i])] += 1
    print(len(d))

if __name__ == '__main__':
    main()