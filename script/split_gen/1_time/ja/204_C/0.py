def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    ans = 0
    for i in range(M):
        for j in range(M):
            if i==j:
                continue
            if (A[i]==A[j] and B[i]==B[j]) or (A[i]==B[j] and B[i]==A[j]):
                ans += 1
    print(ans)
