def main():
    #入力
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    
    #処理
    for i in range(N):
        if S[i] in T:
            print("Yes")
        else:
            print("No")
    
    #出力
    #print(S)
    #print(T)

if __name__ == '__main__':
    main()