def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[X-1] == X:
            ans = i + 1
            break
        X = A[X-1]
    print(ans)
