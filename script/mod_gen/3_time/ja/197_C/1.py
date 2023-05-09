def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 2**30
    for i in range(N):
        for j in range(i, N):
            tmp = 0
            for k in range(i, j+1):
                tmp = tmp | A[k]
            ans = min(ans, tmp)
    print(ans)

if __name__ == '__main__':
    main()