def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    ans = 2**30
    for i in range(N):
        for j in range(i, N):
            x = 0
            for k in range(i, j+1):
                x = x | A[k]
            ans = min(ans, x)
    print(ans)
main()

if __name__ == '__main__':
    main()