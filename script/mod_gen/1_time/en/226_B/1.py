def main():
    N = int(input())
    d = {}
    for i in range(N):
        a = list(map(int, input().split()))
        a = tuple(a[1:])
        if a in d:
            d[a] += 1
        else:
            d[a] = 1
    print(len(d))

if __name__ == '__main__':
    main()