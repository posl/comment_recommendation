def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    visited = [0] * N
    current = 0
    for i in range(K):
        if visited[current]:
            break
        visited[current] = i + 1
        current = A[current] - 1
    else:
        print(current + 1)
        return
    cycle = i + 1 - visited[current]
    K -= visited[current]
    K %= cycle
    for i in range(K):
        current = A[current] - 1
    print(current + 1)

if __name__ == '__main__':
    main()