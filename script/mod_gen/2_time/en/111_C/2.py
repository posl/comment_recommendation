def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    print(n - d[0][1] - d[1][1])

if __name__ == '__main__':
    main()