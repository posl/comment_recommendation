def main():
    A, B, K = map(int, input().split())
    ans = ""
    while A > 0 or B > 0:
        if A == 0:
            ans += "b"
            B -= 1
        elif B == 0:
            ans += "a"
            A -= 1
        else:
            ab = 1
            for i in range(1, A + B):
                ab *= i
            for i in range(1, A):
                ab //= i
            for i in range(1, B):
                ab //= i
            if K <= ab:
                ans += "a"
                A -= 1
            else:
                ans += "b"
                B -= 1
                K -= ab
    print(ans)
