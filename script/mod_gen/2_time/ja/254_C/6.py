def main():
    #入力
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    
    #昇順に並べ替える
    A.sort()
    
    #K番目の要素の値がK番目の要素の値以上ならYes、そうでなければNo
    if A[K-1] >= A[K]:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()