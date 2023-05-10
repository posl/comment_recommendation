def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    sumA = sum(A)
    n = X // sumA
    X -= sumA * n
    ans = n * N
    for i in range(N):
        X -= A[i]
        ans += 1
        if X < 0:
            break
    print(ans)
