def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i, N):
            for k in range(1, 10**5+1):
                if all([A[l] >= k for l in range(i, j+1)]):
                    ans = max(ans, k*(j-i+1))
    print(ans)

if __name__ == '__main__':
    main()