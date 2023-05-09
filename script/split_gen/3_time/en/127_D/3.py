def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = []
    C = []
    for _ in range(M):
        b, c = map(int, input().split())
        B.append(b)
        C.append(c)
    A.sort()
    B, C = (list(t) for t in zip(*sorted(zip(B, C), key=lambda x: x[1], reverse=True)))
    ans = 0
    for i in range(N):
        if i < M:
            if A[i] < C[i]:
                ans += C[i]
            else:
                ans += A[i]
        else:
            ans += A[i]
    print(ans)
