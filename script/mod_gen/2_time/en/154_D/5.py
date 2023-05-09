def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    p = [x + 1 for x in p]
    p = [x / 2 for x in p]
    p_sum = sum(p[:K])
    ans = p_sum
    for i in range(K, N):
        p_sum = p_sum - p[i - K] + p[i]
        ans = max(ans, p_sum)
    print(ans)

if __name__ == '__main__':
    main()