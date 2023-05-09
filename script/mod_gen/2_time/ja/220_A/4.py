def main():
    #入力
    A,B,C = map(int,input().split())
    
    #処理
    ans = -1
    for i in range(A,B+1):
        if i%C == 0:
            ans = i
            break
    #出力
    print(ans)

if __name__ == '__main__':
    main()