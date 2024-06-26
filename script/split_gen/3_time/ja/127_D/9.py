def main():
    # input
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = []
    for i in range(M):
        BC.append(list(map(int, input().split())))
    # compute
    A.sort()
    BC.sort(key=lambda x: x[1], reverse=True)
    i, j = 0, 0
    while i<N and j<M:
        if A[i] < BC[j][1]:
            A[i] = BC[j][1]
            BC[j][0] -= 1
            if BC[j][0] == 0:
                j += 1
            i += 1
        else:
            break
    # output
    print(sum(A))
