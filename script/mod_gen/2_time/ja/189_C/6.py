def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    ans = 0
    for i in range(N):
        for j in range(i+1, N+1):
            x = min(A[i:j])
            ans = max(ans, x*(j-i))
    print(ans)

if __name__ == '__main__':
    main()