def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.append(A[0] + M)
    D = []
    for i in range(N):
        D.append(A[i + 1] - A[i])
    D.sort(reverse=True)
    print(sum(D[N-1:]))

if __name__ == '__main__':
    main()