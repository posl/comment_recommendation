def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    # まずは全員に均等に配る
    for i in range(N):
        a[i] += K // N
    # 残りの配る数
    K = K % N
    # 配る
    for i in range(K):
        # 最小の人に配る
        m = min(a)
        for j in range(N):
            if a[j] == m:
                a[j] += 1
                break
    for i in range(N):
        print(a[i])

if __name__ == '__main__':
    main()