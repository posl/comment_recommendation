def main():
    # 入力
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0] * M
    Y = [0] * M
    for i in range(M):
        X[i], Y[i] = map(int, input().split())
    
    # 準備
    ans = "Yes"
    h = T
    for i in range(N-1):
        h -= A[i]
        if h <= 0:
            ans = "No"
            break
        for j in range(M):
            if i+1 == X[j]:
                h += Y[j]
                break
    # 出力
    print(ans)

if __name__ == '__main__':
    main()