def problem240_d():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    ans = []
    for i in range(n):
        d[a[i]] = d.get(a[i], 0) + 1
        if d[a[i]] % a[i] == 0:
            d.pop(a[i])
        ans.append(len(d))
    print('\n'.join(map(str, ans)))

if __name__ == '__main__':
    problem240_d()