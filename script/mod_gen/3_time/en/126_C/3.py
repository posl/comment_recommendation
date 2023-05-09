def main():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N+1):
        if i >= K:
            ans += 1/N
        else:
            ans += 1/N*(0.5)**(K/i)
    print(ans)

if __name__ == '__main__':
    main()