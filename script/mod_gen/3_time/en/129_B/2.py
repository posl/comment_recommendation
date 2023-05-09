def main():
    N = int(input())
    W = list(map(int, input().split()))
    ans = 1000000000000000000
    for i in range(1, N):
        ans = min(ans, abs(sum(W[:i]) - sum(W[i:])))
    print(ans)
main()

if __name__ == '__main__':
    main()