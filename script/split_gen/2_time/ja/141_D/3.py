def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    discount = [0] * M
    for i in range(M):
        discount[i] = 2 ** i
    ans = 0
    for i in range(N):
        if A[i] >= discount[M-1]:
            ans += A[i]
        else:
            for j in range(M):
                if A[i] >= discount[j]:
                    ans += A[i] // discount[j]
                    break
    print(ans)
