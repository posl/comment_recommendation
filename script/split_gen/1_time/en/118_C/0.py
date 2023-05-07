def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = A[0]
    for i in range(1, N):
        ans = (ans + A[i] - 1) // A[i] * A[i]
    print(ans)
