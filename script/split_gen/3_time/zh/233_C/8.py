def main():
    # N, X = map(int, input().split())
    # L = []
    # for i in range(N):
    #     L.append(list(map(int, input().split())))
    N, X = 3, 200
    L = [[3, 10, 10, 10], [3, 10, 10, 10], [5, 2, 2, 2, 2]]
    # N, X = 3, 1000000000000000000
    # L = [[2, 1000000000, 1000000000], [2, 1000000000, 1000000000], [2, 1000000000, 1000000000]]
    L2 = []
    for i in range(N):
        L2.append([1])
        for j in range(1, L[i][0] + 1):
            L2[i].append(L2[i][j - 1] * L[i][j])
    print(L2)
    count = 0
    for i in range(N):
        for j in range(L[i][0]):
            if X % L2[i][j] == 0 and X // L2[i][j] <= L[i][0]:
                count += L[i][0] - X // L2[i][j]
    print(count)
