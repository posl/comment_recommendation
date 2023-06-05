def getShortestPath(N, X, Y):
    if N == 3:
        return [3, 0]
    elif N == 1:
        return [0]
    elif N == 2:
        return [2, 0]
    else:
        if X == 1:
            if Y == N:
                return [N, N-1, N-2, N-3, N-4, N-5]
            else:
                return [N, N-1, N-2, N-3, N-4, N-5, N-4, N-3, N-2, N-1]
        elif Y == N:
            return [N, N-1, N-2, N-3, N-4, N-5, N-4, N-3, N-2, N-1]
        else:
            return [N, N-1, N-2, N-3, N-4, N-5, N-4, N-3, N-2, N-1, N-2, N-1, N-2, N-3, N-4, N-5, N-4, N-3, N-2, N-1]
N, X, Y = map(int, input().split())
path = getShortestPath(N, X, Y)
for i in range(N-1):
    print(path[i])

if __name__ == '__main__':
    getShortestPath()