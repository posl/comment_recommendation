def comb(n, r):
    if n - r < r:
        return comb(n, n - r)
    else:
        ans_mul = 1
        ans_div = 1
        for i in range(r):
            ans_mul *= n - i
            ans_div *= i + 1
        return ans_mul // ans_div
n, a, b = map(int, input().split())
ans = pow(2, n, 10**9 + 7) - 1
ans -= comb(n, a)
ans -= comb(n, b)
print(ans % (10**9 + 7))

if __name__ == '__main__':
    comb()