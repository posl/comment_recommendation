def main():
    N, K = map(int, input().split())
    D = []
    A = []
    for i in range(K):
        d = int(input())
        D.append(d)
        A.append(list(map(int, input().split())))
    result = N
    for i in range(K):
        for j in range(D[i]):
            if A[i][j] == result:
                result -= 1
                break
    print(result)
