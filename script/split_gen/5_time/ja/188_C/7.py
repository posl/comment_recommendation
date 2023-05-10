def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N, A)
    # 1回戦
    # 1回戦で勝ち残った選手の番号を格納するリスト
    # 1回戦はAを2つずつ比較して大きい方を勝ち残らせる
    # 勝ち残った選手の番号をリストに格納
    B = []
    for i in range(0, 2**N, 2):
        if A[i] > A[i+1]:
            B.append(i)
        else:
            B.append(i+1)
    #print(B)
    # 2回戦以降
    # 2回戦以降は、1回戦で勝ち残った選手の番号を2つずつ比較して大きい方を勝ち残らせる
    # 勝ち残った選手の番号をリストに格納
    for i in range(1, N):
        #print(i)
        C = []
        for j in range(0, 2**(N-i), 2):
            if A[B[j]] > A[B[j+1]]:
                C.append(B[j])
            else:
                C.append(B[j+1])
        B = C
        #print(B)
    #print(B)
    # 最後に負けるのは、準優勝する選手
    if A[B[0]] > A[B[1]]:
        print(B[1]+1)
    else:
        print(B[0]+1)
