def main():
    #入力
    N = int(input())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    #処理
    A_min = min(A)
    B_min = min(B)
    A_min_index = A.index(A_min)
    B_min_index = B.index(B_min)
    if A_min_index == B_min_index:
        A.remove(A_min)
        B.remove(B_min)
        A_min = min(A)
        B_min = min(B)
    #出力
    print(min(A_min + B_min, max(A_min, B_min)))

if __name__ == '__main__':
    main()