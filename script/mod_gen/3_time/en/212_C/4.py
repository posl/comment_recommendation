def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A = sorted(A)
    B = sorted(B)
    ans = 10**9
    i = 0
    j = 0
    while i < N and j < M:
        ans = min(ans, abs(A[i] - B[j]))
        if A[i] > B[j]:
            j += 1
        else:
            i += 1
    print(ans)

if __name__ == '__main__':
    main()