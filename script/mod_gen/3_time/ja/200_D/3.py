def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [x % 200 for x in a]
    d = dict()
    for i, x in enumerate(a):
        if x in d:
            d[x].append(i + 1)
        else:
            d[x] = [i + 1]
    for x in d:
        if len(d[x]) >= 2:
            print('Yes')
            print(len(d[x]), *d[x][:2])
            print(len(d[x]), *d[x][2:])
            return
    print('No')

if __name__ == '__main__':
    main()