def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    X = X - 1
    ans = 1
    visited = [False] * N
    visited[X] = True
    while True:
        X = A[X] - 1
        if visited[X] == True:
            ans = -1
            break
        ans += 1
        visited[X] = True
        if ans == N:
            break
    print(ans)
