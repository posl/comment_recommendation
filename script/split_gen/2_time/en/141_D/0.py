def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = 0
    for i in range(N):
        ans += A[i] // (2 ** M)
        A[i] %= (2 ** M)
        A.sort(reverse=True)
        for j in range(M):
            if A[j] == 0:
                break
            ans += 1
            A[j] -= 1
            A.sort(reverse=True)
    print(ans)
