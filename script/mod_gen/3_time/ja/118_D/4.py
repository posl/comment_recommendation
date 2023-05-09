def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = ''
    while N > 0:
        for i in range(M):
            if N - (A[i] - 1) * 2 >= 0:
                ans += str(A[i])
                N -= (A[i] - 1) * 2
                break
    print(ans)

if __name__ == '__main__':
    main()