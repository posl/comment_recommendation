def main():
    N = int(input())
    #N個の従業員のA_i,B_iをリストに格納
    A_B = [list(map(int,input().split())) for _ in range(N)]
    #A_i,B_iをそれぞれリストに格納
    A = [A_B[i][0] for i in range(N)]
    B = [A_B[i][1] for i in range(N)]
    #A_i,B_iの最小値をそれぞれ求める
    A_min = min(A)
    B_min = min(B)
    #A_i,B_iの最小値の和
    A_B_min = A_min + B_min
    #A_i,B_iのリストの中でA_B_minより小さい数があるかを確認
    if A_B_min > min(A+B):
        print(A_B_min)
    else:
        print(min(A+B))
