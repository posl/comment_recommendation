def main():
    N = int(input())
    A = list(map(int, input().split()))
    # Aの要素の個数をカウント
    A_count = [0] * (N+1)
    for a in A:
        A_count[a] += 1
    # 答えを求めて出力
    for a in A:
        print(sum(A_count) - A_count[a] - 1)

if __name__ == '__main__':
    main()