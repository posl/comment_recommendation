def main():
    N, M, Q = map(int, input().split())
    data = [list(map(int, input().split())) for i in range(Q)]
    A = [1]
    max_score = 0
    while A[0] <= M:
        if len(A) == N:
            score = 0
            for i in range(Q):
                if A[data[i][1]-1] - A[data[i][0]-1] == data[i][2]:
                    score += data[i][3]
            if score > max_score:
                max_score = score
        A[-1] += 1
        for i in range(len(A)-1, 0, -1):
            if A[i] > M:
                A[i-1] += 1
                A[i] = A[i-1]
    print(max_score)

if __name__ == '__main__':
    main()