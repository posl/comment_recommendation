def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    i = 0
    j = 0
    ans = 10 ** 9 + 1
    while i < N and j < M:
        if A[i] < B[j]:
            ans = min(ans, B[j] - A[i])
            i += 1
        else:
            ans = min(ans, A[i] - B[j])
            j += 1
    print(ans)

if __name__ == '__main__':
    main()