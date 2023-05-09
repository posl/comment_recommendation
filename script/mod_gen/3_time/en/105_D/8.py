def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # A[i]をMで割った余りをA[i]に入れる
    for i in range(N):
        A[i] %= M
    # 余りの累積和をA[i]に入れる
    for i in range(1, N):
        A[i] += A[i-1]
        A[i] %= M
    # 余りの出現回数をカウントする
    counter = [0] * M
    for i in range(N):
        counter[A[i]] += 1
    # 余りの出現回数が2以上のものを組み合わせる
    ans = 0
    for i in range(M):
        ans += counter[i] * (counter[i]-1) // 2
    print(ans)

if __name__ == '__main__':
    main()