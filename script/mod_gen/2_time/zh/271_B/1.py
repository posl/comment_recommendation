def main():
    n, q = map(int, input().split())
    a = []
    for i in range(n):
        tmp = list(map(int, input().split()))
        a.append(tmp[1:])
    for i in range(q):
        s, t = map(int, input().split())
        print(a[s-1][t-1])

if __name__ == '__main__':
    main()