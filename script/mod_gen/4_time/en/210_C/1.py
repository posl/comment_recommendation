def main():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    s = set()
    for i in range(k):
        s.add(c[i])
    m = len(s)
    for i in range(k, n):
        s.remove(c[i-k])
        s.add(c[i])
        m = max(m, len(s))
    print(m)

if __name__ == '__main__':
    main()