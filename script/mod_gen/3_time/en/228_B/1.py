def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    visited = [False] * (N + 1)
    count = 0
    while not visited[X]:
        visited[X] = True
        X = A[X]
        count += 1
    print(count)

if __name__ == '__main__':
    main()