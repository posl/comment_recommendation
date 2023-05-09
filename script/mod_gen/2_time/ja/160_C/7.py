def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    # 1 周の移動距離を求める
    d = [A[i + 1] - A[i] for i in range(N - 1)]
    d.append(K - A[N - 1] + A[0])
    # 最短移動距離を求める
    print(K - max(d))

if __name__ == '__main__':
    main()