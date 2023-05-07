def main():
    N, Q = map(int, input().split())
    A = list(range(1, N+1))
    for _ in range(Q):
        x = int(input())
        A[x-1], A[x] = A[x], A[x-1]
    print(*A)

if __name__ == '__main__':
    main()