def S(n):
    ans = 0
    while n > 0:
        ans += n % 10
        n = n // 10
    return ans
A, B = map(int, input().split())
print(max(S(A), S(B)))
