def get_honest_count(N, A, X, Y):
    honest_count = 0
    for i in range(N):
        if A[i] == 0:
            honest_count += 1
        else:
            honest = True
            for j in range(A[i]):
                if X[i][j] > 0 and Y[i][j] != A[X[i][j] - 1]:
                    honest = False
                    break
            if honest:
                honest_count += 1
    return honest_count
N = int(input())
A = []
X = []
Y = []
for i in range(N):
    A.append(int(input()))
    X.append([])
    Y.append([])
    for j in range(A[i]):
        x, y = map(int, input().split())
        X[i].append(x)
        Y[i].append(y)
print(get_honest_count(N, A, X, Y))

if __name__ == '__main__':
    get_honest_count()