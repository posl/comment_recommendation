def func():
    A, B, K = map(int, input().split())
    def comb(a, b):
        if b == 0 or a == b:
            return 1
        if b == 1 or b == a - 1:
            return a
        return comb(a - 1, b - 1) + comb(a - 1, b)
    ans = ""
    while A + B > 0:
        if A == 0:
            ans += "b"
            B -= 1
            continue
        if B == 0:
            ans += "a"
            A -= 1
            continue
        if K <= comb(A + B - 1, B):
            ans += "a"
            A -= 1
        else:
            ans += "b"
            K -= comb(A + B - 1, B)
            B -= 1
    print(ans)
