def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    # A の要素の和を求める
    A_sum = sum(A)
    # A の要素を X にした時の操作回数を求める
    for x in X:
        print(A_sum - N * x)

if __name__ == '__main__':
    main()