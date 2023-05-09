def main():
    import sys
    input = sys.stdin.readline
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    #累積和
    p_sum = [0]
    for i in range(N):
        p_sum.append(p_sum[i] + (p[i]+1)/2)
    #print(p_sum)
    #最大値を求める
    max = 0
    for i in range(N-K+1):
        if max < p_sum[i+K]-p_sum[i]:
            max = p_sum[i+K]-p_sum[i]
    print(max)

if __name__ == '__main__':
    main()