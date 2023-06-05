def main():
    N = int(input())
    A = [0] * N
    B = [0] * N
    for i in range(N-1):
        A[i], B[i] = map(int, input().split())
        A[i] -= 1
        B[i] -= 1
    ans = [0] * (2*N-1)
    for i in range(N-1):
        ans[i] = A[i]
        ans[2*N-2-i] = B[i]
    for i in range(2*N-1):
        print(ans[i]+1, end=' ')
    print()
