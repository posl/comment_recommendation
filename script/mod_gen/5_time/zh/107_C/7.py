def main():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 10**9
    for i in range(N-K+1):
        if x[i]*x[i+K-1] <= 0:
            ans = min(ans, min(-x[i], x[i+K-1])*2+max(-x[i], x[i+K-1]))
        else:
            ans = min(ans, max(x[i], x[i+K-1]))
    print(ans)

if __name__ == '__main__':
    main()