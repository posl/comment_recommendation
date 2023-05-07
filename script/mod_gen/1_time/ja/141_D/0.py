def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    for i in range(M):
        A[i] = A[i] // 2
    print(sum(A))

if __name__ == '__main__':
    main()