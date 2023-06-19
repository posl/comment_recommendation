def f1(n, m, k, s, p):
    ans = 0
    for i in range(2 ** n):
        a = [0] * m
        for j in range(n):
            if i & (1 << j):
                for l in range(k[j]):
                    a[s[j][l] - 1] += 1
        if all(a[i] % 2 == p[i] for i in range(m)):
            ans += 1
    return ans

if __name__ == '__main__':
    f1()