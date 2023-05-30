def solve():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A = A[::-1]
    B = B[::-1]
    left = 0
    right = 0
    for i in range(N):
        left += A[i] / B[i]
        right += A[i]
    right /= 2
    for i in range(N):
        if right >= A[i]:
            right -= A[i]
            left -= A[i] / B[i]
        else:
            left -= right / B[i]
            break
    return left
print(solve())
