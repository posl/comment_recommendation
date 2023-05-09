def main():
    N = int(input())
    W = [int(i) for i in input().split()]
    s = sum(W)
    ans = s
    for i in range(1, N):
        ans = min(ans, abs(2 * sum(W[:i]) - s))
    print(ans)

if __name__ == '__main__':
    main()