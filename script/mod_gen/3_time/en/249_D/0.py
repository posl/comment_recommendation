def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            if A[i] == A[j]:
                continue
            if A[i] % A[j] == 0:
                ans += A.count(A[i] // A[j])
    print(ans)

if __name__ == '__main__':
    main()