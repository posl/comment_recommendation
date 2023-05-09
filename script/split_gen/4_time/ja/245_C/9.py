def solve():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    #A,Bの差の絶対値がK以下であることを確認する
    for i in range(N):
        if abs(A[i] - B[i]) > K:
            print("No")
            exit()
    print("Yes")
