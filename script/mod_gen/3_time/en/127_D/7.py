def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = [list(map(int, input().split())) for _ in range(M)]
    BC.sort(key=lambda x: x[1], reverse=True)
    #print(BC)
    for i in range(M):
        B, C = BC[i]
        if B >= N:
            A = [C] * N
            break
        else:
            for j in range(N):
                if A[j] < C:
                    A[j] = C
                    B -= 1
                    if B == 0:
                        break
                else:
                    break
    print(sum(A))

if __name__ == '__main__':
    main()