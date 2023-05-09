def main():
    H,W = map(int,input().split())
    A = [list(map(int,input().split())) for _ in range(H)]
    #Aの平均を求める
    sum_A = 0
    for i in range(H):
        for j in range(W):
            sum_A += A[i][j]
    ave = sum_A/(H*W)
    #print(ave)
    #Aの平均との差を求める
    diff = [[0 for _ in range(W)] for _ in range(H)]
    for i in range(H):
        for j in range(W):
            diff[i][j] = A[i][j] - ave
    #print(diff)
    #Aの平均との差の絶対値の合計を求める
    sum_diff = 0
    for i in range(H):
        for j in range(W):
            sum_diff += abs(diff[i][j])
    print(int(sum_diff/2))
