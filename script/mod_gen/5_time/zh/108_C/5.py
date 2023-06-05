def main():
    N, K = map(int, input().split())
    ans = 0
    # a + b, b + c, c + a がすべて K の倍数
    # a + b, b + c, c + a のそれぞれが K の倍数
    # a + b, b + c, c + a のそれぞれを K で割った余りが 0
    # a + b, b + c, c + a のそれぞれを K で割った余りの和が 0
    for i in range(1, N + 1):
        ans += (i % K) * ((N + K - i) // K)
        if K % 2 == 0:
            ans += (i % K) * (((N + K // 2 - i) // K) - ((N + K - i) // K))
    print(ans)

if __name__ == '__main__':
    main()