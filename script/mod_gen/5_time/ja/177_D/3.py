def main():
    n, m = map(int, input().split())
    p = [i for i in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        p[a] = min(p[a], p[b])
        p[b] = min(p[a], p[b])
    print(len(set(p)))

if __name__ == '__main__':
    main()