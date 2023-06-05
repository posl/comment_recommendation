def problem200_c():
    N = int(input())
    A = list(map(int, input().split()))
    d = {}
    for a in A:
        mod = a % 200
        if mod in d:
            d[mod] += 1
        else:
            d[mod] = 1
    ans = 0
    for k in d:
        n = d[k]
        ans += n * (n - 1) // 2
    print(ans)

if __name__ == '__main__':
    problem200_c()