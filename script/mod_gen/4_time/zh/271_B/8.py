def main():
    n, q = map(int, input().split())
    #print(n, q)
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    #print(a)
    for i in range(q):
        s, t = map(int, input().split())
        print(a[s-1][t-1])

if __name__ == '__main__':
    main()