def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    ans = 10**10
    for i in range(N):
        ans = min(ans, abs(A[i] - (i+1)))
    print(ans)

if __name__ == '__main__':
    main()