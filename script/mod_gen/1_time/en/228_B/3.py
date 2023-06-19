def main():
    N, X = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    A = [a-1 for a in A]
    X -= 1
    ans = 0
    visited = [False]*N
    while not visited[X]:
        visited[X] = True
        X = A[X]
        ans += 1
    print(ans)
main()
