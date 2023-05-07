def main():
    #入力
    N = int(input())
    A = list(map(int,input().split()))
    #処理
    if N%2 == 0:
        for i in range(N):
            if i%2 == 0:
                A[i] = abs(A[i])
            else:
                A[i] = -abs(A[i])
    else:
        for i in range(N):
            if i%2 == 0:
                A[i] = -abs(A[i])
            else:
                A[i] = abs(A[i])
    print(sum(A))

if __name__ == '__main__':
    main()