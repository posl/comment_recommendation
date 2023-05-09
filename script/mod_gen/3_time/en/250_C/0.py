def main():
    N, Q = map(int, input().split())
    A = [i for i in range(1, N+1)]
    for _ in range(Q):
        x = int(input()) - 1
        A[x], A[x+1] = A[x+1], A[x]
    print(*A)

if __name__ == '__main__':
    main()