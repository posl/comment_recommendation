def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = ""
    while N > 0:
        for i in range(M):
            if N >= A[i]:
                ans += str(A[i])
                N -= A[i]
                break
    print(ans)
