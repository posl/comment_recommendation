def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = [list(map(int, input().split())) for i in range(M)]
    A.sort()
    BC.sort(key=lambda x: x[1], reverse=True)
    i = 0
    for j in range(M):
        while BC[j][0] > 0 and i < N and A[i] < BC[j][1]:
            A[i] = BC[j][1]
            BC[j][0] -= 1
            i += 1
    print(sum(A))
