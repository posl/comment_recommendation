def main():
    N, K = map(int, input().split())
    C = list(map(int, input().split()))
    ans = 0
    color = [0] * 1000010
    for i in range(N):
        color[C[i]] += 1
        if i >= K:
            color[C[i-K]] -= 1
        ans = max(ans, len([i for i in color if i > 0]))
    print(ans)

if __name__ == '__main__':
    main()