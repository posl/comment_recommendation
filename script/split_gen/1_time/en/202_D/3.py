def main():
    A, B, K = map(int, input().split())
    S = A + B
    ans = ""
    for i in range(S):
        if A == 0:
            ans += "b"
            continue
        if B == 0:
            ans += "a"
            continue
        tmp = 1
        for j in range(1, A + 1):
            tmp *= (S - j + 1)
            tmp //= j
            if K <= tmp:
                ans += "a"
                A -= 1
                break
            else:
                K -= tmp
                ans += "b"
                B -= 1
    print(ans)
