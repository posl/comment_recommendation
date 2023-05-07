def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    C = [0] * M
    for i in range(N):
        C[A[i]] += 1
    B = [0] * M
    for i in range(M):
        B[i] = C[i] * i
    B.sort()
    B.reverse()
    for i in range(M):
        if B[i] == 0:
            break
        j = i + 1
        while j < M and B[i] > 0:
            if B[j] > 0:
                B[i] -= 1
                B[j] -= 1
            j += 1
    ans = 0
    for i in range(M):
        if B[i] > 0:
            ans += B[i]
    print(ans)
