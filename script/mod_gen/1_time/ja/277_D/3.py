def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a % M for a in A]
    A.sort()
    A = [a + M for a in A]
    A.append(2 * M)
    min_sum = 10 ** 10
    for i in range(N):
        min_sum = min(min_sum, A[i + N] - A[i])
    print(min_sum)

if __name__ == '__main__':
    main()