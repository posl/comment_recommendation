def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = []
    for _ in range(M):
        BC.append(list(map(int, input().split())))
    A.sort()
    BC.sort(key=lambda x: x[1], reverse=True)
    BC = BC[:N]
    i = 0
    for j in range(N):
        if A[j] < BC[i][1]:
            A[j] = BC[i][1]
            BC[i][0] -= 1
            if BC[i][0] == 0:
                i += 1
            if i == M:
                break
    print(sum(A))
