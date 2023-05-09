def main():
    #入力
    N,X = map(int,input().split())
    #A_i,B_iを格納するリスト
    A = []
    B = []
    #A_i,B_iを格納
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    #合計金額
    sum = 0
    #A_iとB_iを合計
    for i in range(N):
        sum += A[i]*B[i]
    #合計金額がX円以上ならYes
    if sum >= X:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()