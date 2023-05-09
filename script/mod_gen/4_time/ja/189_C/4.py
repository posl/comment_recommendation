def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for l in range(N):
        x = A[l]
        for r in range(l,N):
            if x > A[r]:
                x = A[r]
            ans = max(ans, x*(r-l+1))
    print(ans)
main()

if __name__ == '__main__':
    main()