def solve():
    A, B, K = map(int, input().split())
    import math
    def comb(a, b):
        return math.factorial(a + b) // (math.factorial(a) * math.factorial(b))
    ans = ''
    while A + B > 0:
        if A == 0:
            ans += 'b'
            B -= 1
            continue
        if B == 0:
            ans += 'a'
            A -= 1
            continue
        if K <= comb(A - 1, B):
            ans += 'a'
            A -= 1
        else:
            ans += 'b'
            K -= comb(A - 1, B)
            B -= 1
    print(ans)

if __name__ == '__main__':
    solve()