def main():
    N, Q = map(int, input().split())
    A = list(range(1, N+1))
    for _ in range(Q):
        x = int(input())
        i = A.index(x)
        A[i], A[i+1] = A[i+1], A[i]
    print(*A)

if __name__ == '__main__':
    main()