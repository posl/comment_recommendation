def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a - 1 for a in A]
    B = [0] * N
    B[X - 1] = 1
    for i in range(N):
        if B[i] == 1:
            B[A[i]] = 1
    print(sum(B))

if __name__ == '__main__':
    main()