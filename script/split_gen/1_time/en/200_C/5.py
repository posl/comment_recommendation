def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    ans = 0
    mod = 200
    d = {}
    for i in range(N):
        if i == 0:
            d[A[i] % mod] = 1
        else:
            tmp = {}
            for key in d.keys():
                if (key + A[i]) % mod in tmp.keys():
                    tmp[(key + A[i]) % mod] += d[key]
                else:
                    tmp[(key + A[i]) % mod] = d[key]
            if A[i] % mod in tmp.keys():
                tmp[A[i] % mod] += 1
            else:
                tmp[A[i] % mod] = 1
            d = tmp
    for key in d.keys():
        ans += d[key] * (d[key] - 1) // 2
    print(ans)
