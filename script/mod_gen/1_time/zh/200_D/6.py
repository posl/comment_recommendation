def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a = [0] + a
    a = [sum(a[:i]) % 200 for i in range(1, n + 1)]
    d = {}
    for i in range(n):
        if a[i] in d:
            d[a[i]].append(i)
        else:
            d[a[i]] = [i]
    for k, v in d.items():
        if len(v) >= 2:
            print('Yes')
            print(1, v[0] + 1)
            print(1, v[1] + 1)
            return
    for k, v in d.items():
        if len(v) >= 3:
            print('Yes')
            print(1, v[0] + 1)
            print(2, v[1] + 1, v[2] + 1)
            return
    print('No')

if __name__ == '__main__':
    solve()