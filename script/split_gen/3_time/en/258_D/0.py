def main():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A = sorted(A)
    B = sorted(B)
    A.append(10**9)
    B.append(10**9)
    ans = 0
    i = 0
    j = N - 1
    while X > 0:
        if A[i] < B[j]:
            ans += A[i]
            X -= 1
            i += 1
        else:
            ans += B[j]
            X -= 1
            j -= 1
    print(ans)
