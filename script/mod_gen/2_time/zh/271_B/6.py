def main():
    n, q = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split()))[1:])
    for i in range(q):
        s, t = map(int, input().split())
        print(a[s-1][t-1])

if __name__ == '__main__':
    main()