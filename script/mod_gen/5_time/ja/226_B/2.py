def main():
    n = int(input())
    d = {}
    for i in range(n):
        l = list(map(int, input().split()))
        l.pop(0)
        l = tuple(l)
        if l in d:
            d[l] += 1
        else:
            d[l] = 1
    print(len(d))

if __name__ == '__main__':
    main()