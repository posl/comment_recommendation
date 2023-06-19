def main():
    n, m = map(int, input().split())
    l = []
    r = []
    for _ in range(m):
        a, b = map(int, input().split())
        l.append(a)
        r.append(b)
    print(max(0, min(r) - max(l) + 1))

if __name__ == '__main__':
    main()