def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = []
    for i in range(M):
        BC.append(list(map(int, input().split())))
    A.sort()
    BC.sort(key=lambda x: x[1], reverse=True)
    j = 0
    for i in range(N):
        if j == M:
            break
        if A[i] < BC[j][1]:
            A[i] = BC[j][1]
            BC[j][0] -= 1
            if BC[j][0] == 0:
                j += 1
        else:
            break
    print(sum(A))

if __name__ == '__main__':
    main()