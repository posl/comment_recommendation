def main():
    n = int(input())
    ans = 0
    d = {}
    for _ in range(n):
        l = list(map(int, input().split()))
        l = l[1:]
        if tuple(l) in d:
            d[tuple(l)] += 1
        else:
            d[tuple(l)] = 1
    print(len(d))
    return

if __name__ == '__main__':
    main()