def main():
    #入力
    H, W = map(int, input().split())
    
    #マスの状態を入力
    C = []
    for i in range(H):
        C.append(input())
    #箱の数を数える
    X = [0] * W
    for i in range(H):
        for j in range(W):
            if C[i][j] == "#":
                X[j] += 1
    
    #出力
    print(*X)

if __name__ == '__main__':
    main()