def main():
    #入力
    #S_1,S_2,...,S_{10} は問題文中の方法で生成されうるそれぞれ長さ 10 の文字列
    S = []
    for i in range(10):
        S.append(input())
    #A,B,C,Dを求める
    A = 0
    B = 0
    C = 0
    D = 0
    for i in range(10):
        for j in range(10):
            if S[i][j] == '#':
                if A == 0:
                    A = i + 1
                    C = j + 1
                B = i + 1
                D = j + 1
    #出力
    print(A,B)
    print(C,D)

if __name__ == '__main__':
    main()