def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A = [i-1 for i in A]
    visited = [False]*N
    visited[X-1] = True
    count = 1
    current = X-1
    while True:
        current = A[current]
        if visited[current]:
            print(-1)
            break
        else:
            visited[current] = True
            count += 1
            if current == 0:
                print(count)
                break

if __name__ == '__main__':
    main()