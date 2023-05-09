def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    #print(A)
    #print(B)
    #print(N, M)
    #print(A)
    #print(B)
    #print("N:", N)
    #print("M:", M)
    # 1からNまでの配列を作る
    arr = [i for i in range(1, N+1)]
    #print(arr)
    # 隣り合っているかのチェック
    for i in range(M):
        #print("A[i]:", A[i])
        #print("B[i]:", B[i])
        #print("arr[A[i]-1]:", arr[A[i]-1])
        #print("arr[B[i]-1]:", arr[B[i]-1])
        #print("arr[A[i]]:", arr[A[i]])
        #print("arr[B[i]]:", arr[B[i]])
        if abs(arr[A[i]-1] - arr[B[i]-1]) != 1:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()