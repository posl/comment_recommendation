def main():
    #入力
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    
    #転置行列を求める
    B = []
    for i in range(W):
        B.append([A[j][i] for j in range(H)])
    
    #出力
    for i in range(W):
        print(*B[i])
main()

if __name__ == '__main__':
    main()