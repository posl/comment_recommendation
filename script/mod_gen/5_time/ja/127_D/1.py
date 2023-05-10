def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = [list(map(int, input().split())) for _ in range(M)]
    A.sort()
    BC.sort(key=lambda x: x[1], reverse=True)
    i = 0
    j = 0
    while j < M:
        if i >= N:
            break
        if BC[j][1] <= A[i]:
            break
        else:
            for k in range(BC[j][0]):
                if i >= N:
                    break
                if BC[j][1] <= A[i]:
                    break
                A[i] = BC[j][1]
                i += 1
            j += 1
    print(sum(A))

if __name__ == '__main__':
    main()