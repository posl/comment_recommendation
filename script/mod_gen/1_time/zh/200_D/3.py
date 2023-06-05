def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [0] + a
    a = [i % 200 for i in a]
    d = {}
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if a[i] == a[j]:
                print('Yes')
                print(1, i)
                print(1, j)
                return
            if a[i] in d:
                d[a[i]].append(i)
            else:
                d[a[i]] = [i]
    for k, v in d.items():
        if len(v) >= 2:
            print('Yes')
            print(len(v), v[0], v[1])
            print(len(v), v[2], v[3])
            return
    print('No')

if __name__ == '__main__':
    main()