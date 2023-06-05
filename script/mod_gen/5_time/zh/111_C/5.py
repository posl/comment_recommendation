def main():
    n = int(input())
    v = list(map(int, input().split()))
    v1 = v[0::2]
    v2 = v[1::2]
    c1 = max(v1, key=v1.count)
    c2 = max(v2, key=v2.count)
    if c1 != c2:
        print(n - max(v1.count(c1), v2.count(c2)))
    else:
        print(min(n - v1.count(c1) - v2.count(c2), n - v1.count(c1) - v2.count(c2) - 1))

if __name__ == '__main__':
    main()