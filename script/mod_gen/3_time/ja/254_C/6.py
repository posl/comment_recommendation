def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, K)
    #print(A)
    #昇順であるかどうかを判定する
    def isAsc(A):
        for i in range(1, N):
            if A[i-1] > A[i]:
                return False
        return True
    #昇順であるならばYes, そうでないならばNoを出力する
    if isAsc(A):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()