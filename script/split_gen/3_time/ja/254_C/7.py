def main():
    #入力
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #昇順になっているかどうか
    isAsc = True
    for i in range(N-1):
        if A[i] > A[i+1]:
            isAsc = False
            break
    #昇順になっている場合はYes
    if isAsc:
        print("Yes")
        return
    #昇順になっていない場合
    #Kの倍数の要素を昇順になるように並び替える
    #Kの倍数の要素を昇順になるように並び替える
    for i in range(0, N, K):
        A[i:i+K] = sorted(A[i:i+K])
    #昇順になっているかどうか
    isAsc = True
    for i in range(N-1):
        if A[i] > A[i+1]:
            isAsc = False
            break
    #昇順になっている場合はYes
    if isAsc:
        print("Yes")
    else:
        print("No")
