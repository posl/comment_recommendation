def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    X -= 1
    A = [a-1 for a in A]
    ans = 0
    visited = [0] * N
    while 1:
        if visited[X] == 1:
            ans = -1
            break
        ans += 1
        visited[X] = 1
        X = A[X]
        if visited[X] == 1:
            break
    print(ans)
