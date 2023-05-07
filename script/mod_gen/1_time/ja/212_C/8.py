def main():
    # 入力
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 処理
    A.sort()
    B.sort()
    # 出力
    print(min([abs(A[i]-B[j]) for i in range(N) for j in range(M)]))

if __name__ == '__main__':
    main()