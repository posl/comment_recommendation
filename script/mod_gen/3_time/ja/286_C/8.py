def main():
    N, A, B = map(int, input().split())
    S = input()
    #print(N, A, B, S)
    #print(S[0], S[1])
    #print(S[0:2])
    #print(S[0:2] == S[2:4])
    #文字数が奇数の場合
    if N % 2 == 1:
        #前半と後半が同じかどうか判定
        if S[0:int(N/2)] == S[int(N/2+1):N][::-1]:
            print(0)
        else:
            print(min(A, B))
    #文字数が偶数の場合
    else:
        #前半と後半が同じかどうか判定
        if S[0:int(N/2)] == S[int(N/2):N][::-1]:
            print(0)
        else:
            #前半と後半が同じ文字数かどうか判定
            if S[0:int(N/2)] == S[int(N/2):N]:
                print(B)
            else:
                print(min(A, B))

if __name__ == '__main__':
    main()