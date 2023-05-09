def main():
    n = int(input())
    names = []
    for i in range(n):
        names.append(input())
    d = {}
    for name in names:
        if name not in d:
            d[name] = 1
        else:
            d[name] += 1
    print(max(d, key=d.get))

if __name__ == '__main__':
    main()