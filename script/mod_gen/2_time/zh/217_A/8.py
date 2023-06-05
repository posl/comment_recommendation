def main():
    n, m = map(int, input().split())
    k = []
    a = []
    for i in range(m):
        k.append(int(input()))
        a.append(list(map(int, input().split())))
    print(n, m)
    print(k)
    print(a)

if __name__ == '__main__':
    main()