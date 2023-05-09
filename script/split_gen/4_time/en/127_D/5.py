def main():
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = []
    for _ in range(M):
        BC.append(list(map(int, input().split())))
    BC.sort(key=lambda x: x[1], reverse=True)
    for i in range(M):
        if BC[i][0] >= N:
            for j in range(N):
                A[j] = BC[i][1]
            break
        else:
            for j in range(BC[i][0]):
                A[j] = BC[i][1]
            N -= BC[i][0]
    print(sum(A))
