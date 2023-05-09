def solve():
    N = int(input())
    if N < 10:
        return N
    s = str(N)
    n = len(s)
    ans = 0
    for i in range(1, 1 << n):
        a = 0
        b = 0
        for j in range(n):
            if i & (1 << j):
                a = a * 10 + int(s[j])
            else:
                b = b * 10 + int(s[j])
        if a and b:
            ans = max(ans, a * b)
    return ans
print(solve())

if __name__ == '__main__':
    solve()