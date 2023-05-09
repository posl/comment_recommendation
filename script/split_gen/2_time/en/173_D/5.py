def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if N == 2:
        print(A[0])
        return
    ans = A[0] + A[1]
    for i in range(2, N):
        ans += A[i] * (i // 2)
    print(ans)
