def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(K):
        if N >= A[i]:
            N -= A[i]
            ans += A[i]
        else:
            ans += N
            break
    print(ans)
