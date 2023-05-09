def main():
    A, B, K = map(int, input().split())
    S = A + B
    ans = [0] * S
    for i in range(S):
        if A == 0:
            ans[i] = "b"
            B -= 1
        elif B == 0:
            ans[i] = "a"
            A -= 1
        else:
            if i == 0:
                if K <= comb(A + B - 1, A - 1):
                    ans[i] = "a"
                    A -= 1
                else:
                    ans[i] = "b"
                    B -= 1
                    K -= comb(A + B + 1, A)
            else:
                if ans[i - 1] == "a":
                    if K <= comb(A + B - 1, A - 1):
                        ans[i] = "a"
                        A -= 1
                    else:
                        ans[i] = "b"
                        B -= 1
                        K -= comb(A + B + 1, A)
                else:
                    if K <= comb(A + B - 1, A):
                        ans[i] = "a"
                        A -= 1
                        K -= comb(A + B + 1, A + 1)
                    else:
                        ans[i] = "b"
                        B -= 1
    print("".join(ans))
