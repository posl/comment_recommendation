def main():
    #入力
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #出力
    if N == K:
        print("Yes")
    elif K % 2 == 0:
        if A[K//2] == A[K//2-1]:
            print("Yes")
        else:
            print("No")
    else:
        if A[K//2] == A[K//2+1]:
            print("Yes")
        else:
            print("No")
