def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    AB = []
    for i in range(N):
        AB.append((A[i], B[i]))
    AB.sort(key=lambda x: x[1], reverse=True)
    AB.sort(key=lambda x: x[0], reverse=True)
    result = []
    for i in range(X):
        result.append(AB[i])
    AB = AB[X:]
    AB.sort(key=lambda x: x[1], reverse=True)
    for i in range(Y):
        result.append(AB[i])
    AB = AB[Y:]
    AB.sort(key=lambda x: x[0] + x[1], reverse=True)
    for i in range(Z):
        result.append(AB[i])
    result.sort(key=lambda x: x[0] + x[1], reverse=True)
    result.sort(key=lambda x: x[1], reverse=True)
    result.sort(key=lambda x: x[0], reverse=True)
    for i in range(len(result)):
        print(A.index(result[i][0]) + 1)
