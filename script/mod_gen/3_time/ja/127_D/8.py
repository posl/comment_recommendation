def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    BC = [list(map(int,input().split())) for _ in range(M)]
    A.sort()
    BC.sort(key=lambda x: x[1], reverse=True)
    idx = 0
    for i in range(M):
        for _ in range(BC[i][0]):
            if A[idx] < BC[i][1]:
                A[idx] = BC[i][1]
                idx += 1
                if idx == N:
                    break
            else:
                break
        if idx == N:
            break
    print(sum(A))

if __name__ == '__main__':
    main()