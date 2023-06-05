def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    BC = [list(map(int, input().split())) for _ in range(M)]
    BC.sort(key=lambda x: x[1], reverse=True)
    i = 0
    ans = 0
    for j in range(M):
        if BC[j][0] + i < N:
            ans += BC[j][1] * BC[j][0]
            i += BC[j][0]
        else:
            ans += BC[j][1] * (N - i)
            break
    ans += sum(A[i:])
    print(ans)
