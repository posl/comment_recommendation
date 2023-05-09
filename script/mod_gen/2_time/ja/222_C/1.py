def main():
    N, M = map(int, input().split())
    A = [input() for _ in range(2*N)]
    result = [0 for _ in range(2*N)]
    for i in range(M):
        for j in range(N):
            if A[2*j][i] == "G" and A[2*j+1][i] == "C":
                result[2*j] += 1
            elif A[2*j][i] == "C" and A[2*j+1][i] == "P":
                result[2*j] += 1
            elif A[2*j][i] == "P" and A[2*j+1][i] == "G":
                result[2*j] += 1
            elif A[2*j][i] == "G" and A[2*j+1][i] == "P":
                result[2*j+1] += 1
            elif A[2*j][i] == "C" and A[2*j+1][i] == "G":
                result[2*j+1] += 1
            elif A[2*j][i] == "P" and A[2*j+1][i] == "C":
                result[2*j+1] += 1
        rank = sorted(result, reverse=True)
        for j in range(2*N):
            result[j] = rank.index(result[j]) + 1
    for i in range(2*N):
        print(result.index(i+1)+1)

if __name__ == '__main__':
    main()