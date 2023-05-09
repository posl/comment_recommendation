def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    X -= 1
    ans = 0
    visited = [False] * N
    visited[X] = True
    while not visited[A[X]-1]:
        X = A[X] - 1
        visited[X] = True
        ans += 1
    print(ans)
