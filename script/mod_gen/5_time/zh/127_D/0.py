def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    BC = []
    for i in range(M):
        BC.append(list(map(int, input().split())))
    BC.sort(key=lambda x: x[1], reverse=True)
    i = 0
    for j in range(M):
        if BC[j][0] < N:
            for k in range(BC[j][0]):
                if A[i+k] > BC[j][1]:
                    break
                A[i+k] = BC[j][1]
            i += BC[j][0]
        else:
            for k in range(N):
                if A[i+k] > BC[j][1]:
                    break
                A[i+k] = BC[j][1]
            i += N
        if i >= N:
            break
    print(sum(A))

if __name__ == '__main__':
    solve()