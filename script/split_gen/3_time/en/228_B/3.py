def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a - 1 for a in A]
    X -= 1
    ans = 0
    visited = [False] * N
    while True:
        if visited[X]:
            ans = -1
            break
        ans += 1
        visited[X] = True
        X = A[X]
        if visited[X]:
            break
    print(ans)
