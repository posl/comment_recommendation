def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    X = X - 1
    count = 0
    visited = [False] * N
    while True:
        if visited[X]:
            print(-1)
            return
        if X == 1:
            print(count)
            return
        visited[X] = True
        count += 1
        X = A[X] - 1

if __name__ == '__main__':
    main()