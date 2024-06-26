def main():
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    if N % 2 == 1:
        ans = B[N // 2] - A[N // 2] + 1
    else:
        ans = min(B[N // 2] + B[N // 2 - 1], A[N // 2] + A[N // 2 - 1]) - max(A[N // 2], B[N // 2]) + 1
    print(ans)
