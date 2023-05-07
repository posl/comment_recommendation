def main():
    N = int(input())
    S = input()
    Q = int(input())
    T = [0] * Q
    A = [0] * Q
    B = [0] * Q
    for i in range(Q):
        T[i], A[i], B[i] = map(int, input().split())
    ans = S
    rev = False
    for i in range(Q):
        if T[i] == 1:
            if rev:
                A[i] = (A[i] + N - 1) % (2 * N) + 1
                B[i] = (B[i] + N - 1) % (2 * N) + 1
            A[i] -= 1
            B[i] -= 1
            ans = ans[:A[i]] + ans[B[i]] + ans[A[i] + 1:B[i]] + ans[A[i]] + ans[B[i] + 1:]
        else:
            rev = not rev
    if rev:
        ans = ans[N:] + ans[:N]
    print(ans)
