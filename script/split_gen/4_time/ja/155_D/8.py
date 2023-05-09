def solve():
    # まずは入力を受け取る
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # ここからコードを書く
    A.sort()
    #print(A)
    #print(A[K-1])
    print(A[K-1])
