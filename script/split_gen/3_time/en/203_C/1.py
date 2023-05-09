def main():
    N, K = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    A = A + [10**100]
    B = B + [0]
    A = A + [10**100]
    B = B + [0]
    A, B = zip(*sorted(zip(A, B)))
    A = list(A)
    B = list(B)
    #print(A)
    #print(B)
    ans = 0
    for i in range(N + 1):
        if K < A[i] - ans:
            ans += K
            break
        else:
            K -= A[i] - ans
            ans = A[i]
            K += B[i]
    print(ans)
