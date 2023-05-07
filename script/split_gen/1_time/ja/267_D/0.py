def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = []
    for i in range(N-M+1):
        B.append(sum(A[i:i+M]))
    B.sort(reverse=True)
    ans = 0
    for i in range(M):
        ans += (i+1)*B[i]
    print(ans)
