def main():
    #入力
    H,W = map(int,input().split())
    #print(H,W)
    A = [list(map(int,input().split())) for _ in range(H)]
    #print(A)
    #最小値を求める
    min_A = min([min(A[i]) for i in range(H)])
    #print(min_A)
    #最小値を引いた値を出力
    print(sum([sum([A[i][j]-min_A for j in range(W)]) for i in range(H)]))

if __name__ == '__main__':
    main()