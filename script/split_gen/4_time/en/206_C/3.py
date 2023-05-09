def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += N - A.index(A[i]) - 1
        A = A[A.index(A[i]) + 1:]
    print(ans)
