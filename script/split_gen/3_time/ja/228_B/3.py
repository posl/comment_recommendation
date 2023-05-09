def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a-1 for a in A]
    visited = [0] * N
    visited[X-1] = 1
    #print(A)
    #print(visited)
    for i in range(N):
        if visited[A[X-1]] == 1:
            break
        visited[A[X-1]] = 1
        X = A[X-1]+1
    print(sum(visited))
