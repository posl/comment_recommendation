def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    visited = [False] * (N + 1)
    visited[X] = True
    count = 0
    while True:
        X = A[X]
        if visited[X] == True:
            break
        else:
            visited[X] = True
            count += 1
    print(count)

if __name__ == '__main__':
    main()