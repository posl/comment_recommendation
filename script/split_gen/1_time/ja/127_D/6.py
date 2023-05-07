def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = [list(map(int, input().split())) for _ in range(M)]
    BC.sort(key=lambda x: x[1], reverse=True)
    ans = 0
    for i in range(M):
        for j in range(BC[i][0]):
            if A:
                if BC[i][1] > A[0]:
                    ans += BC[i][1]
                    A.pop(0)
                    continue
            ans += BC[i][1]
            break
    ans += sum(A)
    print(ans)
