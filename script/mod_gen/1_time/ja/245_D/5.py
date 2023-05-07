def main():
    #入力
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    #処理
    B = [0] * (M + 1)
    for i in range(M + 1):
        B[i] = C[i] // A[0]
    #出力
    print(*B)

if __name__ == '__main__':
    main()