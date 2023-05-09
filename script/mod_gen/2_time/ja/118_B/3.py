def main():
    N, M = map(int, input().split())
    d = [0] * M
    for _ in range(N):
        *A, = map(int, input().split())
        for a in A[1:]:
            d[a-1] += 1
    print(sum(1 for i in d if i == N))

if __name__ == '__main__':
    main()