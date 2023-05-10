def main():
    N, W = map(int, input().split())
    T = 2 * 10 ** 5 + 1
    A = [0 for _ in range(T)]
    for _ in range(N):
        S, T, P = map(int, input().split())
        A[S] += P
        A[T] -= P
    for i in range(T):
        A[i + 1] += A[i]
    for i in range(T):
        if A[i] > W:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()