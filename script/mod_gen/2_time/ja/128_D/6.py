def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for left in range(min(N, K) + 1):
        for right in range(min(N, K) - left + 1):
            gems = V[:left] + V[N - right:]
            gems.sort()
            tmp = sum(gems)
            for i in range(min(left + right, K - left - right)):
                if gems[i] < 0:
                    tmp -= gems[i]
                else:
                    break
            ans = max(ans, tmp)
    print(ans)

if __name__ == '__main__':
    main()