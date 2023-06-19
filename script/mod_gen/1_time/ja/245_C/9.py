def main():
    #入力
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    #出力
    if (A[0] == B[0] and A[-1] == B[-1]):
        print("Yes")
    elif (A[0] == B[0] and A[-1] != B[-1]):
        if (A[-1] - A[0] <= K):
            print("Yes")
        else:
            print("No")
    elif (A[0] != B[0] and A[-1] == B[-1]):
        if (A[-1] - A[0] <= K):
            print("Yes")
        else:
            print("No")
    else:
        if (A[-1] - A[0] <= K):
            print("Yes")
        elif (A[-1] - B[0] <= K):
            print("Yes")
        elif (B[-1] - A[0] <= K):
            print("Yes")
        else:
            print("No")
    
main()
