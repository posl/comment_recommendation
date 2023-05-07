def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = A[::-1]
    ans = 0
    for i in range(N):
        if A[i] <= ans:
            ans = A[i]
        else:
            ans = A[i] - 1
    print(ans)
