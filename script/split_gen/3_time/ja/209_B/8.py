def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    ans = "Yes"
    for i in range(N):
        if i % 2 == 0:
            X -= A[i]
        else:
            X -= A[i] - 1
        if X < 0:
            ans = "No"
            break
    print(ans)
