def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    BC = []
    for _ in range(M):
        BC.append(list(map(int, input().split())))
    BC.sort(key=lambda x: x[1], reverse=True)
    A = A[::-1]
    BC = BC[::-1]
    i = 0
    j = 0
    while i < N and j < M:
        if BC[j][0] == 0:
            j += 1
        else:
            A[i] = BC[j][1]
            BC[j][0] -= 1
            i += 1
    print(sum(A))

if __name__ == '__main__':
    main()